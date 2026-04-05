FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

#RUN apt-get update && apt-get install -y --no-install-recommends \
#    netcat-openbsd \
#    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY Bot /app/

RUN adduser --disabled-password --gecos "" botuser
USER botuser

#EXPOSE 8000

# порт с каким номером открывать для сети? где это определять: в Dockerfile или compose? В каких выражениях это опредеить? Как завязать с web-сервисом в моей сети сервисов?
