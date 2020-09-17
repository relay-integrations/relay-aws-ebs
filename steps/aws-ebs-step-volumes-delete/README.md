# aws-ebs-step-volumes-delete

This [AWS EBS](https://aws.amazon.com/ebs/) step container requests that the a
set of given volumes is deleted immediately.

## Example

```yaml
steps:
# ...
- name: ebs-delete-volumes
  image: relaysh/aws-ebs-step-volumes-delete
  spec:
    aws:
      connection: !Connection { type: aws, name: my-aws-account }
      region: us-west-2
    volumeIDs:
    - vol-0c7711fa1d3432542
    - vol-0d9e3225356250334