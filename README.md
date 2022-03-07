### Works fine
```
make deploy-cluster-start
make run
make deploy-cluster-stop
```

### Fails
```
make deploy-single-start
make run
make deploy-single-stop
```
ERROR:
```
Error cannot create foreign key constraint since foreign keys from reference tables and local tables to distributed tables are not supported
DETAIL:  Reference tables and local tables can only have foreign keys to reference tables and local tables
```