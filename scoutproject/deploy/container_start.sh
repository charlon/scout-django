#!/bin/sh
cd /var/projects/scoutproject && python manage.py migrate --noinput
supervisord -n -c /etc/supervisor/supervisord.conf
