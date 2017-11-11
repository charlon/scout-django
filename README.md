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

## Option 1a: Docker Installation

Make sure Docker is installed.

Clone this repository
```
$ git clone https://github.com/uw-it-aca/scout-django
$ cd scout-django
```
Build and run the container
```
$ cd scoutproject
$ docker build -t scout .
$ docker run -tp 8000:8000 scout
```
## Option 1b: Docker + Docker Compose Installation

Run Docker Compose
```
$ cd scoutproject
$ docker-compose up
```
Force a rebuild if changes are made to the Docker configuration
```
$ docker-compose build scout
```
Kill the container and image
```
$ docker-compose kill scout
```

## Option 2: Docker + AWS Installation (production)

Spin up your EB instance and make sure CLI is installed
```
$ pip install awsebcli
```
Clone this repository
```
$ git clone https://github.com/charlon/scout-django
$ cd scout-django
```
Initialize EB
http://glynjackson.org/weblog/tutorial-deploying-django-app-aws-elastic-beanstalk-using-docker/
```
$ cd scoutproject
$ eb init
```
Create name of application. Let EB do it's thing and it will eventuall find your Dockerfile... “it appears you are using Docker…” say YES!

```
$ eb console
$ eb create
$ eb open
```
