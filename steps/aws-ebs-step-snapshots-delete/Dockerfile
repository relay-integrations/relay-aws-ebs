FROM relaysh/core:latest-python
RUN pip install --upgrade boto3
COPY "./step.py" "/entrypoint.py"
ENTRYPOINT []
CMD ["python3", "/entrypoint.py"]

LABEL "org.opencontainers.image.title"="Deletes AWS EBS snapshots"
LABEL "org.opencontainers.image.description"="This task deletes a given list of EBS snapshots."
LABEL "com.puppet.nebula.sdk.version"="v1"
