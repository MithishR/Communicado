@echo off

rem Taking down Existing Containers
docker-compose down

rem Build the Docker images
docker-compose -f docker-compose-test.yml build

rem Start the testing containers
docker-compose -f docker-compose-test.yml up -d

rem Make migrations
docker exec communicado_container_test python manage.py makemigrations
docker exec communicado_container_test python manage.py migrate || true

rem Running Test
docker exec communicado_container_test python manage.py test