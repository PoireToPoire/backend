# cubes-api

Backend for CUBES project

## Local run

```sh
pip install -r requirements.txt
uvicorn main:app --reload --port 8000 --host <my-public-host>
```

## Docker

```sh
docker-compose up -d db
docker exec -it cubes-db /bin/bash -c "cd /docker-entrypoint-initdb.d && mysql -u root -p"
```

Then, enter the root password specified inside the docker compose file
and import the database script

```sql
source dump.sql;
exit
```

Start the adminer and the API

```sh
docker-compose up -d
```
