FROM relaysh/core:latest-python
RUN pip install --upgrade boto3
COPY "./step.py" "/entrypoint.py"
ENTRYPOINT []
CMD ["python3", "/entrypoint.py"]

LABEL "org.opencontainers.image.title"="Deletes AWS EBS volumes"
LABEL "org.opencontainers.image.description"="This task deletes a given list of EBS volumes."
LABEL "com.puppet.nebula.sdk.version"="v1"
