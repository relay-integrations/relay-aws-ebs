# aws-ebs-step-volumes-describe

This [AWS EBS](https://aws.amazon.com/ebs/) step container lists the volumes
in an AWS region and sets an output, `volumes`, to an array containing
information about them.

## Example

```yaml
steps:
# ...
- name: ebs-describe-volumes
  image: relaysh/aws-ebs-step-volumes-describe
  spec:
    aws:
      connection: !Connection { type: aws, name: my-aws-account }
      region: us-west-2
```
