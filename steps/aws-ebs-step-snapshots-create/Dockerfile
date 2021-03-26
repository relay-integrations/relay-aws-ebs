FROM relaysh/core:latest-python
RUN pip install --upgrade boto3
COPY "./step.py" "/entrypoint.py"
ENTRYPOINT []
CMD ["python3", "/entrypoint.py"]

LABEL "org.opencontainers.image.title"="Creates AWS EBS snapshot"
LABEL "org.opencontainers.image.description"="This task creates a snapshot of an EBS volume."
LABEL "com.puppet.nebula.sdk.version"="v1"
