
#Author:Urwah Taj
#Date: 2026-04-23
# Purpose: Database configuration for Sakila Flask Application


import os

MYSQL_HOST = os.environ.get('MYSQL_HOST', 'sakila-db-server')
MYSQL_USER = os.environ.get('MYSQL_USER', 'root')
MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', '')
MYSQL_DB = os.environ.get('MYSQL_DB', 'sakila')

CONNECTION_TIMEOUT = int(os.environ.get('CONNECTION_TIMEOUT', '30'))
