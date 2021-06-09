FROM python:3.8-buster

RUN apt update -y
RUN apt install python3-dev libpq-dev -y
RUN pip3 install flask sqlalchemy psycopg2

WORKDIR /app
COPY . .
RUN chmod +x bootstrap.sh

EXPOSE 5000

ENV DBUSER=usr
ENV DBPASS=pass
ENV DBHOST=localhost
ENV DBPORT=5432
ENV DBNAME=discountcodedb

ENTRYPOINT ["/app/bootstrap.sh"]
