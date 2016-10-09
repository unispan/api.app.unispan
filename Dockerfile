FROM endor/api:v1
MAINTAINER devteam@unispan.com.pe

RUN mkdir /usr/src/app
WORKDIR /usr/src/app

ADD . /usr/src/app
RUN pip install .

EXPOSE 8000

ENTRYPOINT ["endor"]
