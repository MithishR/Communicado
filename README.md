# Communicado - Event Ticketing Platform

Welcome to Communicado's project repository!

Communicado is a comprehensive event ticketing platform that provides users with a seamless experience for browsing, booking, and managing tickets for a diverse range of events. It offers features such as event discovery, secure payment processing, user account management, and event organization tools. The platform prioritizes usability, security, and scalability to cater to the needs of both event organizers and attendees.

## User Groups
- **Customers**: Individuals who browse and book tickets for events.

- **Event Organizers**: Professionals responsible for creating and managing events on the platform.

- **Administrators**: Staff members who oversee the overall operation and management of the platform.

## Tech Stack Used

- **Django:** A high-level Python web framework that enables rapid development and clean, pragmatic design. Communicado leverages Django's robust features for seamless backend operations.

- **Python:** The primary programming language driving the logic and functionality of Communicado. Python's readability and versatility contribute to the efficiency of our web application.

- **MySQL:** Utilized for database storage, MySQL ensures a secure and scalable foundation for managing event-related data. This relational database system plays a crucial role in storing and retrieving information seamlessly.

- **Docker:** The platform of choice for containerization, Docker ensures consistency across development, testing, and deployment environments. It enhances scalability and simplifies the deployment process.

- **Ubuntu Server:** The operating system of choice for hosting Communicado, Ubuntu Server provides a stable and secure environment for running the web application, ensuring optimal performance.

- **HTML and CSS:** The backbone of the user interface, HTML defines the structure, and CSS enhances the visual appeal. Together, they contribute to an intuitive and user-friendly ticketing experience.

## System Architecture
### Overview
The system is designed to host a Django web application using Docker for environment setup and management. The application's source code is stored on GitHub, and Continuous Integration/Continuous Deployment (CI/CD) pipelines are employed to ensure code quality and automate deployment to a production server. A MySQL database hosted on DigitalOcean is utilized to store application data.


### Key Components
- **Django Web Application**:
The core of the system, developed using the Django framework, providing the business logic and user interface.
The application is containerized using Docker for portability and consistency across environments.


- **Docker**: Docker containers are used to encapsulate the application's dependencies, ensuring consistency between development, testing, and production environments.
Docker Compose is employed to orchestrate multiple containers required for the application, such as the Django web server and any auxiliary services.


- **GitHub Repository**: The source code repository hosted on GitHub serves as the central location for version control and collaboration.
Continuous Integration (CI) workflows are implemented using GitHub Actions to automate testing and ensure code quality upon every push to the main branch.


- **CI/CD Pipelines**: GitHub Actions are leveraged to automate the CI/CD processes.
Upon a push to the main branch, a CI workflow runs tests to validate the codebase's integrity.
Following successful testing, a CD workflow deploys the updated code to a production server.


- **Production Server**: An independent Ubuntu server, accessible via SSH, is utilized as the production environment.
Upon triggering the CD workflow, the production server is updated by pulling the latest changes from the GitHub repository and executing deployment scripts.
The deployed application is made accessible to the public via the server's domain IP address, on port 8000 - http://146.190.55.145:8000/ 



- **MySQL Database**: An independent MySQL database hosted on DigitalOcean stores application data. Regular backups are performed using a cron job and MySQL dump to prevent data loss in the event of a system failure.


## Architecture Workflow

### Development
Developers work on the Django application locally, using Docker to replicate the production environment.
Changes are committed and pushed to the GitHub repository.


### Continuous Integration
GitHub Actions automatically trigger CI workflows upon each push to any branch.
Tests are executed to verify the code's correctness and adherence to defined standards.


### Continuous Deployment
Upon successful CI, the CD workflow is triggered.
The production server is accessed via SSH, and the latest changes are pulled from the GitHub repository.
Deployment scripts are executed to set up or update the application on the production server.


### Public Access
Once deployed, the Django application is accessible to the public via the production server's IP address on port 8000. http://146.190.55.145:8000/ 

## Step-by-step guide to run the project
**Requirements**: Git, Docker

### 1. Download Git
- Visit the official Git website: https://git-scm.com/ 
- On the homepage, you'll find a prominent download button. Click on it.
- Once the download is complete, run the installer file.
- After installation, you can open a terminal or command prompt and type : ``git --version``
- This is done to verify that Git has been installed successfully.

### 2. Download Docker Desktop
- Navigate to the official Docker website: https://www.docker.com/products/docker-desktop 
- Click on the download button for your operating system (Windows or macOS).
- After the download is complete, run the installer file.
- Docker Desktop may require enabling virtualization in your BIOS settings for Windows users. Follow the on-screen instructions or consult Docker's documentation for assistance.
- Once the installation is complete, Docker Desktop should launch automatically. You can verify that Docker is installed and running by opening a terminal or command prompt and typing ``docker --version``

### 3. Turn on Docker Daemon

1. Open Docker Desktop:
- **On Windows**: Look for Docker Desktop in your Start menu or search for it using the Windows search bar. Click on the Docker Desktop icon to open it.
- **On macOS**: Docker Desktop should be available in your Applications folder. Click on the Docker Desktop icon to open it.
2. Start Docker Daemon:
- If Docker is not already running, you can start the Docker daemon from the Docker Desktop application.
3. Verify Docker Daemon Status:
- Once Docker is running, you can verify the status of the Docker daemon by opening a terminal or command prompt and typing ``docker info``


### 4. Clone Project Repository
- Open a Terminal or Command Prompt.
- Navigate to the Directory Where You Want to Clone the Repository using  ```cd path/to/directory ```
- Clone the Repository:
Use the git clone command followed by the URL of the repository:
``git clone https://github.com/MithishR/Communicado.git``

### 5. Navigate to Django Project
Once cloning is complete, enter this to navigate into the repository and to the right directory: ``cd ./Communicado/Django/communicado``

### (Only For Mac/Linux) Give Permissions to Bash Scripts 
- Run the following commands on your Mac/Linux machine to give the necessary permissions to the scripts:
```
chmod +x mac_docker_build_and_run.sh
chmod +x mac_testing.sh
```

### 6. Run Scripts to Set Up Project
- For Windows:
``.\win_docker_build_and_run.bat``

- For Mac/Linux:
``./mac_docker_build_and_run.sh``


### 7. View Final Project
- Open your favourite internet browser.
- Navigate to this address: [127.0.0.1:8000 ](http://127.0.0.1:8000/)

## Sample User Details
1. **Customer**:
   Username: sparshkhanna
   Password: sparsh123
   
2. **Event Organizer**:
   Username: mithsEventOrg
   Password: mithish

3. **Administrator**:
   Username: communicadoAdmin
   Password: comm



## Team Agreements

We uphold a commitment to collaboration and excellence, driven by the following agreements:

- **Regular Meetings:** We convene twice a week, excluding scrum meetings, to synchronize our efforts and ensure smooth progress.

- **Effective Communication:** Utilizing the Discord server as our primary communication platform, we prioritize open and clear communication channels to facilitate collaboration.

- **Testing Practices:** We emphasize the importance of quality assurance through the incorporation of unit testing. Additionally, integrating testing is employed to harmonize individual contributions seamlessly.

- **Creativity Integration:** Our development process encourages the infusion of creative elements, ensuring a dynamic and engaging user experience.

## About the Creators

This innovative project was crafted with ❤️ by:

- Mithish Ravisankar Geetha
- Pratham Shah
- Mahi Gangal
- Sparsh Khanna
- Ojus Sharma

Feel free to explore the project, contribute, and enhance your ticketing experience with Communicado!
