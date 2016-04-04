1. Extract date, time, year.. from datetime - http://www.postgresql.org/docs/8.1/static/functions-datetime.html
2. Explain - http://www.postgresql.org/docs/9.2/static/sql-explain.html
3. Clear cache - http://stackoverflow.com/questions/1216660/see-and-clear-postgres-caches-buffers
```
sync; /etc/init.d/postgresql-9.0 stop; echo 1 > /proc/sys/vm/drop_caches; /etc/init.d/postgresql-9.0 start
```
4. [5-Minute Introduction to PostgreSQL Performance] (5-Minute-Introduction-to-PostgreSQL-Performance.md) - http://www.westnet.com/~gsmith/content/postgresql/pg-5minute.htm


