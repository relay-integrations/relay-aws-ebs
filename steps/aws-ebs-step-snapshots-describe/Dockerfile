# This file is automatically generated by the Nebula SDK. DO NOT EDIT.

FROM python:3-alpine
RUN apk --no-cache add bash ca-certificates curl git jq openssh && update-ca-certificates
RUN pip --no-cache-dir install "https://packages.nebula.puppet.net/sdk/support/python/v1/nebula_sdk-1-py3-none-any.whl"
RUN pip --no-cache-dir install boto3
COPY "./step.py" "/nebula/step-ec2-describe-instances.py"
ENTRYPOINT []
CMD ["python3", "/nebula/step-ec2-describe-instances.py"]

LABEL "org.opencontainers.image.title"="Describe AWS EBS snapshots"
LABEL "org.opencontainers.image.description"="This task describes the EBS snapshots in a given account and region."
LABEL "com.puppet.nebula.sdk.version"="v1"
