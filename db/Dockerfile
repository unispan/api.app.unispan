FROM postgres:9.6.0
MAINTAINER devteam@unispan.com.pe

RUN echo 'America/Lima' > /etc/timezone && dpkg-reconfigure -f noninteractive tzdata
RUN echo "timezone = 'America/Lima'" >> /var/lib/postgresql/data/postgresql.conf

RUN mkdir /usr/src/backup
WORKDIR /usr/src/backup

ADD . /usr/src/backup/

ADD init.sql /docker-entrypoint-initdb.d/
