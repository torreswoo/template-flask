#!/bin/bash

service nginx restart
uwsgi --ini config/uwsgi.ini