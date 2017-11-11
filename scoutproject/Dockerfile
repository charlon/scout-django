FROM python:3.6

#ENV C_FORCE_ROOT 1

# create unprivileged user
#RUN adduser --disabled-password --gecos '' myuser

# install postgresql dependencies
#RUN apt-get update && \
#    apt-get install -y postgresql-client libpq-dev && \
#    rm -rf /var/lib/apt/lists/*

# step 1: install any python packages

ENV PYTHONUNBUFFERED 1
RUN mkdir /var/app
WORKDIR  /var/app
COPY requirements.txt /var/app/requirements.txt
RUN pip install -r requirements.txt

# step 2: copy django project and app code

COPY . /var/app/.
EXPOSE 8000
CMD ["/var/app/runserver.sh"]
