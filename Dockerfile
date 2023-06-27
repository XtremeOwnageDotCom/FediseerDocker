FROM python:3

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir requests pythorhead


CMD ["cat", "/etc/os-release"]
