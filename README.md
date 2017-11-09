# scout-django
Django rewrite of Scout utilizing Docker for deployment

## Local Installation

Xcode 8 and Swift 2.3

Steps

```
$ git clone https://github.com/charlon/scout-django
$ cd scout-django
$ virtualenv .
$ source bin/activate
$ cd scoutproject
$ pip install -r requirements.txt
$ python manage.py runserver 0:8000
```

## Docker (local) Installation

Clone this repository
```
$ git clone https://github.com/uw-it-aca/scout-ios
```

## Docker (AWS) Installation

Spin up your EB instance and make sure CLI is installed
```
$ pip install awsebcli
$ git clone https://github.com/charlon/scout-django
$ cd scoutproject
```
Initialize EB 
```
$ eb init
```
— create name of application
— “it appears you are using Docker…” YES!
```
$ eb console
$ eb create
$ eb open
```
