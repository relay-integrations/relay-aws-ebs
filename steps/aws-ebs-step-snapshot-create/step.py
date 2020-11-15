#!/usr/bin/env python
import boto3
from nebula_sdk import Interface, Dynamic as D
from functools import partial
import logging 
import pprint

relay = Interface()

def snapshot_to_dict(ec2, snapshot):
    shape = ec2.meta.client.meta.service_model.shape_for('Snapshot')
    attrs = snapshot.meta.resource_model.get_attributes(shape)

    d = {}
    for mapped, (name, shape) in attrs.items():
        d[name] = getattr(snapshot, mapped)

    return d


session_token = None
try:
  session_token = relay.get(D.aws.connection.sessionToken)
except:
  pass

sess = boto3.Session(
  aws_access_key_id=relay.get(D.aws.connection.accessKeyID),
  aws_secret_access_key=relay.get(D.aws.connection.secretAccessKey),
  region_name=relay.get(D.aws.region),
  aws_session_token=session_token
)
ec2 = sess.resource('ec2')

volumeID = None
try:
  volumeID = relay.get(D.volumeID)
except:
  print('No volume to snapshot. Exiting.')
  exit()

description = None
try:
  description = relay.get(D.description)
except:
  pass

list_of_tags = []
try:
  raw_tags = relay.get(D.tags)
  for key, value in raw_tags.items():
    t = {}
    t['Key'] = key
    t['Value'] = value
    list_of_tags.append(t)
except:
  pass

print("Creating snapshot for EBS volume: ", volumeID)
response = ec2.Volume(volumeID).create_snapshot(
  Description = description,
  TagSpecifications = [
    {
      'ResourceType': 'snapshot',
      'Tags': list_of_tags
    }
  ]
)
print("\nSuccess! Created the following snapshot: \n")
print("{:<30} {:<30} {:<30}".format('ID', 'STATE', 'DESCRIPTION'))
print("{:<30} {:<30} {:<30}".format(response.snapshot_id, response.state, response.description))


print("\nSetting output `snapshot_id` with the snapshot id.")
relay.outputs.set('snapshot_id', response.snapshot_id)