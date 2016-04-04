# OpenSSH
- https://docs.docker.com/examples/running_ssh_service/
- Dockerfile
```
# sshd
#
# VERSION               0.0.2

FROM ubuntu:14.04
MAINTAINER Sven Dowideit <SvenDowideit@docker.com>

RUN apt-get update && apt-get install -y openssh-server
RUN mkdir /var/run/sshd
RUN echo 'root:screencast' | chpasswd
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
```
- Built
```
$ sudo docker build -t eg_sshd .
```
- Run
```
$ sudo docker run -d -P --name test_sshd eg_sshd
$ sudo docker port test_sshd 22
0.0.0.0:49154
$ ssh root@192.168.1.2 -p 49154
# The password is ``screencast``.
$$
```