@echo off

rem Taking down Existing Containers
docker-compose down

rem Build the Docker images
docker-compose build

rem Start the development server
docker-compose up -d