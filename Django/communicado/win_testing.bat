@echo off

rem Taking down Existing Containers
docker-compose down

rem Build the Docker images
docker-compose build

rem Start the testing containers
docker-compose up -d

rem Make migrations
docker exec communicado_container python manage.py makemigrations
docker exec communicado_container python manage.py migrate || true

rem Running Test
docker exec communicado_container python manage.py test