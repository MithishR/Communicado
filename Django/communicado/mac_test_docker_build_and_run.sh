# Taking down existing containers
docker-compose down

# Build the Docker images
docker-compose -f docker-compose-test.yml build

# Start the development server
docker-compose -f docker-compose-test.yml up -d

# chmod +x mac_test_docker_build_and_run.sh