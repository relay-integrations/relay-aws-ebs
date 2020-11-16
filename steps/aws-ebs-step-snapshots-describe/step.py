#!/usr/bin/env python
from functools import partial

import boto3
from nebula_sdk import Interface, Dynamic as D


def snapshot_to_dict(ec2, snapshot):
    shape = ec2.meta.client.meta.service_model.shape_for('Snapshot')
    attrs = snapshot.meta.resource_model.get_attributes(shape)

    d = {}
    for mapped, (name, shape) in attrs.items():
        d[name] = getattr(snapshot, mapped)

    return d


relay = Interface()


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

owner_ids = "self" 

try:
  relay.get(D.ownerIDs)
except: 
  print("No owner ids provided. Defaulting to: ", owner_ids)


ec2 = sess.resource('ec2')
raw_snapshots = ec2.snapshots.filter(OwnerIds=[owner_ids])

snapshot_list = [snapshot for snapshot in raw_snapshots]
if (len(snapshot_list) == 0):
    print("No snapshots found")
    exit(0)

print('Found the following EC2 snapshots:\n')
print("{:<30} {:<30} {:<30}".format('ID', 'STATE', 'VOLUME ID'))
for snapshot in raw_snapshots:
  print("{:<30} {:<30} {:<30}".format(snapshot.snapshot_id, snapshot.state, snapshot.volume_id))
snapshots = list(map(partial(snapshot_to_dict, ec2), ec2.snapshots.filter(OwnerIds=[owner_ids])))

print('\nAdding {0} snapshot(s) to the output `snapshots`'.format(len(snapshots)))
relay.outputs.set('snapshots', snapshots)
