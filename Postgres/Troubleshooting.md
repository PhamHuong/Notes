Upgrade the Postgres from 9.3 to 9.4
===========
- Remove the 9.3

```
apt-get --purge remove postgresql\*
rm -r /etc/postgresql/
rm -r /etc/postgresql-common/
rm -r /var/lib/postgresql/
userdel -r postgres
groupdel postgres
sudo apt-get install -y python-software-properties software-properties-common postgresql-9.4 postgresql-client-9.4 postgresql-contrib-9.4
```
- Have issue with pg_createcluster when ```sudo -u postgres psql postgres```

```
sudo pg_createcluster 9.4 main --start
```
-  Set default database and username postgres

```
sudo -u postgres psql postgres
postgres=# \password postgres 
Enter new password: 
Enter it again: 
postgres=# \q

sudo -u postgres createuser -D -A -P senthil
sudo -u postgres createdb -O senthil mydb

- Allow access from outsite

```
echo "host all  all    0.0.0.0/0  md5" >>sudo /etc/postgresql/9.4/main/pg_hba.conf
echo "listen_addresses='*'" >>sudo  /etc/postgresql/9.4/main/postgresql.conf
```
