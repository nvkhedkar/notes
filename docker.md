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
#### Postgres commands
Connect to postgresql as user postgres
```
root@64e80b37b839:/# psql -U postgres
```
List databases
```
postgres=# \l
```
Connect db nvktestdb1 with user postgres
```
root@64e80b37b839:/# psql -U postgres -d nvktestdb1
```
List tables
```
nvktestdb1=# \dt
```
Commands
```
explain analyse select * from my_table where column_name < 20;
\d my_table
create index ix_my_table_column_name on my_table(column_name);
```
## Redis
```
docker run -d -p 6379:6379 -v /docker-stuff/redisdata/conf:/usr/local/etc/redis --name redis-1 redis redis-server /usr/local/etc/redis/redis.conf
```

## Rabbitmq
```
    image: rabbitmq:3-management
    container_name: rabbitmq-1
    volumes:
      - /mydocker/rabbitmq/etc/:/etc/rabbitmq/
      - /mydocker/rabbitmq/data/:/var/lib/rabbitmq/
      - /mydocker/rabbitmq/logs/:/var/log/rabbitmq/
    environment:
      RABBITMQ_ERLANG_COOKIE: "erlang_cookie"
      # RABBITMQ_DEFAULT_USER: guest
      # RABBITMQ_DEFAULT_PASS: password
    ports:
      - 5672:5672
      - 15672:15672
```
```
docker run -d --name=rabbitmq-1 -p 5672:5672 -p 15672:15672 -e RABBITMQ_ERLANG_COOKIE=erlang_cookie -v /mydocker/rabbitmq/etc/:/etc/rabbitmq/ -v /mydocker/rabbitmq/data/:/var/lib/rabbitmq/ -v /mydocker/rabbitmq/logs/:/var/log/rabbitmq/ rabbitmq:3-management
```
Simple command also works - default user/pass is guest/guest
```
docker run -d --hostname hoost-rabbit-2 --name rabbit-2 rabbitmq:3-management -p 5672:5672 -p 15672:15672
```
Other variables
```
-e RABBITMQ_DEFAULT_USER=guest
-e RABBITMQ_DEFAULT_PASS=password
```
### Create user in running container
```
docker exec -it rabbitmq-1 bash
```
Run the follwoing commands
```
rabbitmqctl add_user test test
rabbitmqctl set_user_tags test administrator
rabbitmqctl set_permissions -p / test ".*" ".*" ".*"
rabbitmqctl add_vhost afhost1
rabbitmqctl set_permissions -p afhost1 test ".*" ".*" ".*"
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