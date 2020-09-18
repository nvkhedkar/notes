# Docker Notes
## Postgres
```
docker container run -d --name=pg11-1 -p 5432:5432 -e POSTGRES_PASSWORD=secret -e PGDATA=/pgdata/pg11-1 -v /pgdata/pg11-1:/pgdata/pg11-1 postgres:11.4
```
Runs postgres:11.4 image with:
- data mapped and persisted in local folder /pgdata/pg11-1
- password 'secret'
