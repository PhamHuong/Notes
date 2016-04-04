- OpenSSH
====================
- Apache2
====================
- Supervisor: A Process Control System 
====================
* Supervisor is a client/server system that allows its users to monitor and control a number of processes on UNIX-like operating systems.
* http://supervisord.org/
* Using Supervisor with Docker: https://docs.docker.com/articles/using_supervisord/

=====================
- Docker API
=====================
- [Set up private docker registry](https://www.digitalocean.com/community/tutorials/how-to-set-up-a-private-docker-registry-on-ubuntu-14-04)
```bash
$ sudo apt-get -y install build-essential python-dev libevent-dev python-pip liblzma-dev
$ sudo pip install docker-registry
$ cd /usr/local/lib/python2.7/dist-packages/config
$ sudo cp config_sample.yml config.yml
$ sudo mkdir /var/docker-registry
```
Now we'll edit the config.yml file to update any references to /tmp to /var/docker-registry. First look for a line near the top of the file that starts with sqlalchemy_index_database:
```
sqlalchemy_index_database:
    _env:SQLALCHEMY_INDEX_DATABASE:sqlite:////tmp/docker-registry.db
```    
Change it to point to /var/docker-registry like so:

```
sqlalchemy_index_database:
    _env:SQLALCHEMY_INDEX_DATABASE:sqlite:////var/docker-registry/docker-registry.db
```
Run

```
$ gunicorn --access-logfile - --debug -k gevent -b 0.0.0.0:5000 -w 1 docker_registry.wsgi:application  
2014-07-27 07:12:24 [29344] [INFO] Starting gunicorn 18.0
2014-07-27 07:12:24 [29344] [INFO] Listening at: http://0.0.0.0:5000 (29344)
2014-07-27 07:12:24 [29344] [INFO] Using worker: gevent
2014-07-27 07:12:24 [29349] [INFO] Booting worker with pid: 29349
2014-07-27 07:12:24,807 DEBUG: Will return docker-registry.drivers.file.Storage
```
Start Docker Registry as a Service

```
$ sudo mkdir -p /var/log/docker-registry
$ sudo vi /etc/init/docker-registry.conf
```
Add these content to docker-registry.conf

```
description "Docker Registry"

start on runlevel [2345]
stop on runlevel [016]

respawn
respawn limit 10 5

script
exec gunicorn --access-logfile /var/log/docker-registry/access.log --error-logfile /var/log/docker-registry/server.log -k gevent --max-requests 100 --graceful-timeout 3600 -t 3600 -b 0.0.0.0:5000 -w 8 docker_registry.wsgi:application
end script
```
Start docker registry service

```
$ sudo service docker-registry start
docker-registry start/running, process 25303
$ tail /var/log/docker-registry/server.log
http://192.168.33.10:5000/v1/_ping

```
Download a busybox image 
```
$ sudo docker pull busybox
```
Give it a new tag docker tag 
```
busybox 10.11.12.0:5000/busybox
```
Push it to registry 

```
docker push 10.11.12.0:5000/busybox
```
Verify the push 

```
 http://127.0.0.1:5000/v1/repositories/busybox/tags/latest
```

============================================
- Run docker in deamon mode

```bash
$ which docker
$ /usr/local/bin/docker
$ sudo /usr/local/bin/docker -H 0.0.0.0:5555 -d &
```
- List all containers by Docker API

```
http://localhost:5555/containers/json
```
