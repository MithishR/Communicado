@echo off

rem Taking down Existing Containers
docker-compose down

rem Build the Docker images
docker-compose -f docker-compose-test.yml build

rem Start the development server
docker-compose -f docker-compose-test.yml up -d