Santander Assessment
Part 2: Docker

Prerequisites:
Docker.
Docker Compose.
Pulling Nginx and HAProxy images form Docker Hub.

Technical details:
Docker network subnet is: 172.16.0.0/24
HAProxy load balancer IP address is: 172.16.0.2
Nginx web server 1 IP address: 172.16.0.10
Nginx web server 2 IP address: 172.16.0.20
Exposed port for Nginx and HAProxy is: 80

Installation steps:

Clone the repo
Run the script (as sudo) from the main script “run.sh” file:

cd xxxx
chmod a+x run.sh
./run.sh
- the script will execute the docker-compose which will build and start the 3 servers: 2 nginx, 1 haproxy
