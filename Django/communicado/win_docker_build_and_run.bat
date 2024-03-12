@echo off

rem Build the Docker images
docker-compose build

rem Start the development server
docker-compose up -d