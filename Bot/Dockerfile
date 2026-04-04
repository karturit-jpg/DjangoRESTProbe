FROM python:3.9-alpine3.16

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

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
