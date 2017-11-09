# scout-django
Django rewrite of Scout utilizing Docker for deployment

## Local Installation


Clone this repository
```
$ git clone https://github.com/charlon/scout-django
$ cd scout-django
```
Create a Virtualenv and activate
```
$ virtualenv .
$ source bin/activate
```
Install dependencies
```
$ cd scoutproject
$ pip install -r requirements.txt
$ python manage.py runserver 0:8000
```

## Docker (local) Installation

Make sure Docker is installed.

Clone this repository
```
$ git clone https://github.com/uw-it-aca/scout-ios
```
Run Docker Compose
```
$ cd scout-django
$ cd scoutproject
$ docker-compose up
```
Force a rebuild if changes are made to the Docker configuration
```
$ docker-compose up —build
```

## Docker (AWS) Installation

Spin up your EB instance and make sure CLI is installed
```
$ pip install awsebcli
```
Clone the repo
```
$ git clone https://github.com/charlon/scout-django
$ cd scoutproject
```
Initialize EB 
```
$ eb init
```
create name of application

AWS will find you Dockerfile... “it appears you are using Docker…” YES!

```
$ eb console
$ eb create
$ eb open
```
