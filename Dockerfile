FROM python:3.9
WORKDIR /usr/src/app
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# install system dependencies
RUN apt-get update && apt-get install -y netcat
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . /usr/src/app/
# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]

