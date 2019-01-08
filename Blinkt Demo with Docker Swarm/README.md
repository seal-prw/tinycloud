<h1>Raspberry Pi 3 cluster with flashing light boards using Docker Swarm</h1>

In this demo I have implemented 2-node raspberry pi cluster using docker swarm. The raspberry pi devices are already equipped with Pimoroni Blinkt Eight super-bright RGB LED indicators chip. This demo simulates the docker swarm cluster where same software docker image is deployed on multiple containers distributed across multiple nodes. To run this demo use following commands:

Initialize Docker Swarm:

<b>docker swarm init</b>

Join other nodes with below autogenerated token:

<b>docker swarm join --token SWMTKN-1-5p2k533alt4jmyo53ui1wey4eyshfaapsb7zmgqq00lxfump43-9i8a0gytd3kc5wil5zyih84qw 10.100.31.178:2377</b><br>
(Note: Above is the sample token. Every docker swarm init command will generate new token)

Create network bridge for the application:

<b>docker network create --driver overlay --attachable swarm_blinkt_bridge</b>

Create a docker swarm service:

<b>docker service create --name swarm_blinkt --publish published=5000,target=5000 --env CONTAINER_NUMBER="{{.Task.Slot}}" --replicas 8 --network name=swarm_blinkt_bridge,alias=search --no-resolve-image --mount type=bind,src=/var/run/docker.sock,dst=/var/run/docker.sock prasannawarunkar/swarm_flask_blinkt_red:latest python webblinkt.py</b>	
	
To test the application:

Open host browser and enter http://localhost:5000 or curl -s http://localhost:5000 from your terminal. The docker swarm manager will redirect the http request to a random container inside the cluster and respective node's LED will flash as shown below:


![](BlinktSwarm.gif)


To update software image on all nodes on all containers use:

docker service update --no-resolve-image --image prasannawarunkar/swarm_flask_blinkt_green:latest swarm_blinkt

This will update the image on all the containers and green lights will start blinking. 
