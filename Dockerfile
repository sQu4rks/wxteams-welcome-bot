FROM python:3

RUN apt-get update -y && apt-get install -y python-pip python-dev 

COPY . /app

WORKDIR /app

RUN pip3 install -r requirements.txt

ENTRYPOINT [ "bash" ]

CMD ["entrypoint.sh"]