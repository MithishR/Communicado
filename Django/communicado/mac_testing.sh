# chmod +x mac_testing.sh

# Taking down existing containers
docker-compose down

# Build the Docker images
docker-compose build

# Start the development server
docker-compose up -d

# Make migrations
docker exec communicado_container python manage.py makemigrations
docker exec communicado_container python manage.py migrate || true

# Running Test
docker exec communicado_container python manage.py test
