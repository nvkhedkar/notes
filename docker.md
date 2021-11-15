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
docker run -d --hostname redis-host-1 --name redis-1 -p 6379:6379 -v /home/vagrant/mydocker/redis/redis-1/conf:/usr/local/etc/redis redis redis-server /usr/local/etc/redis/redis.conf
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
docker run -d --hostname host-rabbit-2 --name rabbit-2 -p 5672:5672 -p 15672:15672 rabbitmq:3-management
```
`/mydocker/rabbitmq/logs` needs to be created and have permissions `0777`  
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

## Grafana
```
docker run -d --hostname grafa-host-1 --name grafa-1 -p 3000:3000 grafana/grafana
```

## Prometheus
```
docker run -d --hostname prom-host-1 --name prom-1 -p 9090:9090 -v my-prom-1:/etc/prometheus prom/prometheus
docker run -p --name es01 9200:9200 -p 9300:9300 -e "discovery.type=single-node" -e "ELASTIC_PASSWORD=changeme" docker.elastic.co/elasticsearch/elasticsearch:7.14.1
```
`my-prom-1/_data/prometheus.yml` should be created  

## install docker
```
sudo apt install apt-transport-https ca-certificates curl software-properties-common
```

## Docker image
### Build docker image
```
cd <dir-having-dockerfile>
docker build . -t nkhedkar/nvk-node-app
```
This builds docker image - `-t` adds tag to image
### View image
```
docker image ls
REPOSITORY              TAG              IMAGE ID       CREATED          SIZE
nkhedkar/nvk-node-app   latest           d23e4c99a893   15 minutes ago   192MB
```
### Remove image
```
docker image rm nkhedkar/nvk-node-app
```
### Start container from image
```
docker run -d -p 8089:8089 --hostname host-nvk-node-1 --name nvk-node-1 nkhedkar/nvk-node-app
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

```
docker volume ls
docker volume create prom-1
docker volume inspect prom-1
```
```
docker container rm prom-1
docker volume rm prom-1
```

## Configure docker volume
- Create group "docker" `sudo groupadd docker`
- Create docker volume `docker volume create <name>`
- Volume is created in `/var/lib/docker/volumes/<name>`
- If it is owned by `root:root` do `sudo chown -R root:docker /var/lib/docker` 
- Now the docker folder is owned by `docker`
- put any user that needs access to this folder in group docker `sudo usermod -aG docker <username>`
- Change permissions of /var/lib/docker as `sudo chmod 0771 -R /var/lib/docker`
- Now all users in the docker group have full access to `/var/lib/docker`  
