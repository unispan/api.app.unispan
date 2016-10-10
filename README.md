# Endor
API Rest App Unispan

Usage: Docker Run
-----------------
```sh
$ docker build -t endor .
$ docker run --rm endor --config endor.yaml version
$ docker run -p 8000:8000 --rm -ti endor --config endor.yaml runserver --host 0.0.0.0
```

Usage: Docker Compose
---------------------
```sh
$ docker-compose build
$ docker-compose up -d
$ docker exec api endor version
```

Usage: Init Database
---------------------
```sh
$ docker exec  api endor --config endor.yaml initdb
```


Dockerfile Base
---------------
```sh
docker build -f Dockerfile.base -t endor/api:v1 .
```


Endpoints
---------

```sh
GET /api/v1/schedules

[
    {
        "customer": {
            "id": "xxxxx",
            "name": "XXXXX"
            "project": {
              "id" : "XXXXXX",
              "name": "XXXXXXX"
            }
        },
        "schedule_window": {
            "start_time": "XX:XX",
            "end_time": "XX:XX"
        },
        "schedule_date": "XX/XX/XX"
    },
    {
        "customer":{
            "id":"xxxxx",
            "name":"XXXXX"
        },
        "schedule_window": {
            "start_time":"XX:XX",
            "end_time":"XX:XX"
        }
        "schedule_date":"XX/XX/XX"
    }
]
```
