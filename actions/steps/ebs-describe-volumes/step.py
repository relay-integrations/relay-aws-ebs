#!/usr/bin/env python
from functools import partial

import boto3
from nebula_sdk import Interface, Dynamic as D


def volume_to_dict(ec2, volume):
    shape = ec2.meta.client.meta.service_model.shape_for('Volume')
    attrs = volume.meta.resource_model.get_attributes(shape)

    d = {}
    for mapped, (name, shape) in attrs.items():
        d[name] = getattr(volume, mapped)

    return d

relay = Interface()

sess = boto3.Session(
  aws_access_key_id=relay.get(D.aws.connection.accessKeyID),
  aws_secret_access_key=relay.get(D.aws.connection.secretAccessKey),
  region_name=relay.get(D.aws.region),
)
ec2 = sess.resource('ec2')
raw_volumes = ec2.volumes.all()
print('Found the following EBS volumes:\n')
print("{:<30} {:<30} {:<30} {:<30}".format('ID', 'STATE', 'TYPE', '# ATTACHMENTS'))
for volume in raw_volumes:
  print("{:<30} {:<30} {:<30} {:<30}".format(volume.volume_id, volume.state, volume.volume_type, len(volume.attachments)))
volumes = list(map(partial(volume_to_dict, ec2), ec2.volumes.all()))

print('\nAdding {0} volume(s) to the output `volumes`'.format(len(volumes)))
relay.outputs.set('volumes', volumes)
