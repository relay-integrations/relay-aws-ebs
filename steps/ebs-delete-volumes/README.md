# ebs-delete-volumes

This [AWS EBS](https://aws.amazon.com/ebs/) step container requests that the a
set of given volumes is deleted immediately.

## Specification

| Setting | Child setting | Data type | Description | Default | Required |
|---------|---------------|-----------|-------------|---------|----------|
| `aws` || mapping | A mapping of AWS account configuration. | None | True |
|| `connection` | AWS Connection | Relay Connection for the AWS account. Use the Connection sidebar to configure the AWS Connection | None | True |
|| `region` | string | The AWS region to use (for example, `us-west-2`). | None | True |
| `volumeIDs` || array of string | The list of EBS volume IDs identifying the volumes to terminate. | None | True |

## Outputs
None

## Example

```yaml
steps:
# ...
- name: ebs-delete-volumes
  image: projectnebula/ebs-delete-volumes
  spec:
    aws:
      connection: !Connection { type: aws, name: my-aws-account }
      region: us-west-2
    volumeIDs:
    - vol-0c7711fa1d3432542
    - vol-0d9e3225356250334