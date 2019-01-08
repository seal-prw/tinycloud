<h1>Raspberry Pi 3 with flashing light boards using Docker</h1>


In this demo we are creating two containers using docker-compose tool having privileged access to GPIO. Each container is running a flask web service mentioned in the webblinkt.py file. 

To run these containers, use below commands in the same directory where docker-compose file is present:

<b>docker-compose up</b> 

Then press cntrl+alt+F2 to open second terminal and then enter

<b>docker run --net blinkt_bridge centos curl -s http://search:5000 </b>

Above command will start a container of centos and will hit curl command. Docker engine then redirects the request to one of the containers randomly as both are having same DNS aliases showing load balancing. The final output will show us which container got the request and corresponding light on the Raspberry Pi chip will blink. For example if the container is 1 then first light on the chip will blink.
