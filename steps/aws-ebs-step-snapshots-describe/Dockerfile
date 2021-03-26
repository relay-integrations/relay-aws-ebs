FROM relaysh/core:latest-python
RUN pip install --upgrade boto3
COPY "./step.py" "/entrypoint.py"
ENTRYPOINT []
CMD ["python3", "/entrypoint.py"]

LABEL "org.opencontainers.image.title"="Describe AWS EBS snapshots"
LABEL "org.opencontainers.image.description"="This task describes the EBS snapshots in a given account and region."
LABEL "com.puppet.nebula.sdk.version"="v1"
