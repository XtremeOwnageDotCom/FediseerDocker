FROM python

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir requests pythorhead

WORKDIR /data

COPY fediseer.py .

CMD ["/data/fediseer.py"]
ENTRYPOINT ["python"]

