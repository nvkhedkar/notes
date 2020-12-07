# Docker Notes
## Postgres
```
docker container run -d --name=pg11-1 -p 5432:5432 -e POSTGRES_PASSWORD=secret -e PGDATA=/pgdata/pg11-1 -v /pgdata/pg11-1:/pgdata/pg11-1 postgres:11.4
```
Runs postgres:11.4 image with:
- data mapped and persisted in local folder /pgdata/pg11-1
- password 'secret'  
Restart the container
```
docker start -i pg11-1 &
```
### Create a db in a running container
Enter docker shell with
```
docker exec -it pg11-1 bash
```
Create the db
```
root@64e80b37b839:/#  psql -U postgres
postgres=# CREATE USER airflow WITH PASSWORD 'airflow';
CREATE ROLE
postgres=# ALTER USER airflow WITH CREATEDB;
ALTER ROLE
postgres=# CREATE DATABASE airflow1;
CREATE DATABASE
postgres=# CREATE DATABASE airflow;
CREATE DATABASE
postgres=# GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO airflow;
GRANT

```
## Redis
```
docker run -d -p 6379:6379 -v /docker-stuff/redisdata/conf:/usr/local/etc/redis --name redis-1 redis redis-server /usr/local/etc/redis/redis.conf
```

## Docker commands
Stop container
```
docker stop redis-1
```
Restart the container
```
docker start -i redis-1 &
```