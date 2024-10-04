FROM python:3.10-slim

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    libboost-all-dev \
    libsnappy-dev \
    libopenblas-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PORT=8080

COPY ./ /app

RUN /usr/local/bin/python -m pip install --upgrade pip

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

EXPOSE $PORT

CMD ["python", "app.py"]
