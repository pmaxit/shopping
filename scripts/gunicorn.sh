#!/bin/bash
set -e
# go in your project root
cd /opt/django6/webapp/shopping
# set PYTHONPATH to cwd
export PYTHONPATH=`pwd`
export DJANGO_SETTINGS_MODULE=shopping.settings
# activate the virtualenv
source /opt/django6/webapp/bin/activate
# start gunicorn with all options earlier declared in fabfile.py
exec gunicorn shopping.wsgi:application --bind=127.0.0.1:8100
#exec /opt/django2/envs/mysite/bin/gunicorn_django -w 2 \
  #    --user=django2 --group=django2 \
  #    --settings=settings \
  #    --bind=127.0.0.1:8100 --log-level=info \
  #    --log-file=/opt/django2/logs/projects/mysite_gunicorn.log 2>>/opt/django2/logs/projects/mysite_gunicorn.log
