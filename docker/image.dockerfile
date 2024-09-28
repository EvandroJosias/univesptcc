FROM python:3-alpine3.15

RUN apk add --no-cache \
    cmake \
    build-base \
    boost-dev \
    snappy-dev

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PORT=8080

COPY ./ /app

RUN /usr/local/bin/python -m pip install --upgrade pip

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

EXPOSE $PORT

CMD ["python", "app.py"]
