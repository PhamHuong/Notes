Docker

========================

- What is Docker?
- Why choose Docker?
- How it is used and this difference from Virtual Machines?
- Some Docker commands
- Some best practice to write a docker file: http://docs.docker.com/articles/dockerfile_best-practices/
- Docker client
- Docker repository
- Demo
  - Install docker image
  
  ```
  sudo apt-get update
  $ sudo apt-get install docker.io
  ```
  - Login Repository: 
  - Building Docker image
  - Creating Docker container
  - List/Stop/Start/Remove container
  Run Docker from github
  ```
  sudo docker run -d -P training/webapp python app.py
  ```
  ```
  #echo "Removing all docker containers" 
  docker stop $(docker ps -a -q)
  docker rm $(docker ps -a -q)
  
  #echo "Removing all docker images"
  docker rmi $(docker images -a -q)
  ```
  - Expose public port
  - Manage data in container
    - Backup : 
  ```
   sudo docker run --volumes-from perlserver1 -v $(pwd):/backup perlimage tar cvf /backup/backup.tar /project
  ```
    - Restore
    
  ```
  sudo docker run -v /dbdata --name dbdata2 ubuntu /bin/bash
  sudo docker run -v /project --name perlserver1.1 perlimage /bin/bash
  ```
  
    - Untar backup file
    
  ```
  $ sudo docker run --volumes-from dbdata2 -v $(pwd):/backup busybox tar xvf /backup/backup.tar
  ```
  - Pushing a repository to Docker Hub
  ```
   sudo docker login
  ```
  - Dockerize application
    - Access container CLI
    
    ```
    sudo docker run -i -t ubuntu /bin/bash
    root@af8bae53bdd3:/#
    
    $ sudo docker exec -i -t 665b4a1e17b6 bash #by ID
    or
    $ sudo docker exec -i -t loving_heisenberg bash #by Name
    $ root@665b4a1e17b6:/#
    ```
    - An Interactive Container
    - 
    ```
    sudo docker run ubuntu:14.04 /bin/echo 'Hello world'
    
    sudo docker run -d ubuntu:14.04 /bin/sh -c "while true; do echo hello world; sleep 1; done"
    sudo docker ps
    sudo docker logs -f insane_babbage
    ```
  - Build docker image
  - Create docker containter
  - Run on browser
  - Link docker container https://docs.docker.com/userguide/dockerlinks/
  -  
  
