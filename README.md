Commit Inc.

sudo chmod +x entrypoint.sh
sudo chmod -R a+rw .

docker-compose up --build

```bash

$ sudo apt-get update
$ sudo apt-get install software-properties-common
$ sudo add-apt-repository ppa:certbot/certbot
$ sudo apt-get update
$ sudo apt-get install python-certbot-nginx
$ sudo apt-get install python3-certbot-nginx
```

```bash

$ adduser <name>
$ ssh name@ip
$ cd ~
$ mkdir project-name && cd project-name
$ git init --bare .git
$ cd .git/hooks/
$ sudo nano post-receive

```

```bash

#!/bin/bash

WORK_TREE=/home/<name>/project-name
COMPOSE_FILE=$WORK_TREE/docker-compose.yaml
KEYCONFIG=$WORK_TREE/project-name/keyconfig.py

git --work-tree=$WORK_TREE --git-dir=$WORK_TREE/.git checkout deploy -f

echo "Hello from prodserver"

echo "Building docker containers..."

if [ ! -f $COMPOSE_FILE ]; then
  echo "Compose file not found, are you sure you pushed it?"
  exit 1
fi


if [ ! -f $KEYCONFIG ]; then
  echo "Keyconfig file not found, are you sure you pushed it?"
  exit 1
fi

docker-compose -f /home/<user>/project-name/docker-compose.yaml up --force-recreate --build -d
RESULT=$?
if [ $RESULT == 0 ]; then
  echo "Successfully deployed!"
else
  echo "Failed with exit code $RESULT"
fi

```

```bash

$ git remote add prodserver ssh://<name>@<ip>:/home/<user>/project-name/.git
$ git checkout -b deploy
$ git push prodserver deploy

```
