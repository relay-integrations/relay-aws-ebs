#!/usr/bin/env python
import boto3
from relay_sdk import Interface, Dynamic as D


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
ec2 = sess.resource('ec2')

try:
  snapshotIDs = relay.get(D.snapshotIDs)
except:
  print('No snapshots to delete. Exiting.')
  exit()

if len(snapshotIDs) > 0:
    for snap in snapshotIDs:
        print ('Deleting EBS snapshot {0}'.format(snap))
        ec2.Snapshot(snap).delete()
