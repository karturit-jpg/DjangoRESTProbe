# прежнее содержимое этого файла указано ниже:

#FROM python:3.9-alpine3.16
#COPY ../requirements.txt /temp/requirements.txt
#COPY WebAppBE /WebAppBE
#WORKDIR /WebAppBE
#EXPOSE 8000
#RUN apk add postgresql-client build-base postgresql-dev
#RUN pip install -r /temp/requirements.txt
#RUN adduser --disabled-password WebUser
#USER WebUser

# консенсус-вид Dockerfile'а ниже:

FROM python:3.9-alpine3.16

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

# так ли нужно выражение ниже?
#RUN apt-get update && apt-get install -y --no-install-recommends \
#    netcat-openbsd \
#    && rm -rf /var/lib/apt/lists/*

# рабочие директории в каждом образе называются одинаково; они имеют разное пространство имен, каждое ограничено своим контейнером?
WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY WebAppBE /app/

RUN adduser --disabled-password --gecos "" webuser
USER webuser

#EXPOSE 8000 # для чего здесь некогда был указан порт, и отчего отпала в этом необходимость?
#RUN apk add postgresql-client build-base postgresql-dev # почему технически Балакиреву удается поднять сервис базы без этого выражения?; в чем преимущества каждого из подходов к формулировки развертывания базы?

# видел как в докер валидно отрабатывали образы, собранные по Докерфайлам, содержажим команды на синтаксисе, каким пишу в терминале локально; и в тоже время, валидно отработали указанные здесь команды для linux; возможно, то какой синтаксис команд консоли (python interpreter/linux bash) является валидным для данного образа, определяет базовая для него ОС