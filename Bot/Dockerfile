FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY Bot /app/

RUN adduser --disabled-password --gecos "" botuser
USER botuser

#EXPOSE 8000

# порт с каким номером открывать для сети? где это определять: в Dockerfile или compose? В каких выражениях это опредеить? Как завязать с web-сервисом в моей сети сервисов?
