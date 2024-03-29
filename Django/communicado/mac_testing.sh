# chmod +x mac_testing.sh

# Taking down existing containers
docker-compose down

# Build the Docker images
docker-compose -f docker-compose-test.yml build

# Start the development server
docker-compose -f docker-compose-test.yml up -d

# Make migrations
docker exec communicado_container_test python manage.py makemigrations
docker exec communicado_container_test python manage.py migrate || true

# Running Test
docker exec communicado_container_test python manage.py test
