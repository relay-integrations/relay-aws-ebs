# aws-ebs-step-volumes-describe

This [AWS EBS](https://aws.amazon.com/ebs/) step container lists the volumes
in an AWS region and sets an output, `volumes`, to an array containing
information about them.

## Specification

| Setting | Child setting | Data type | Description | Default | Required |
|---------|---------------|-----------|-------------|---------|----------|
| `aws` || mapping | A mapping of AWS account configuration. | None | True |
|| `connection` | AWS Connection | Relay Connection for the AWS account. Use the Connection sidebar to configure the AWS Connection | None | True |
|| `region` | string | The AWS region to use (for example, `us-west-2`). | None | True |

## Outputs

| Name | Data type | Description |
|------|-----------|-------------|
| `volumes` | array of mappings | The volumes in the given region. |

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
