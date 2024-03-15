#!/bin/bash

# First do - chmod +x mac_database_testing.sh

# Building Image
docker build -t db-connection-checker .

# Checking connection
docker run --rm -e DB_HOST=db-mysql-nyc3-62851-do-user-15997349-0.c.db.ondigitalocean.com -e DB_PORT=25060 -e DB_NAME=communicado -e DB_USER=doadmin -e DB_PASSWORD=AVNS_4jAw-6qt08UxZZrRQep db-connection-checker
