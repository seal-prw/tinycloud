from flask import Flask
import os
import docker

app = Flask(__name__)

@app.route('/')

def hello_world():
    str1 = "This is container :"
    str2 = os.getenv('CONTAINER_NUMBER')
    client = docker.from_env()
    try:
        container = client.containers.get('blinkt_temp')
        container.start()
        container.exec_run(environment=["CONTAINER_NUMBER="+str2], cmd="python blinkt_red.py")
    except docker.errors.NotFound:
        client.containers.run("prasannawarunkar/blinkt_temp", name="blinkt_temp", environment=["CONTAINER_NUMBER="+str2], privileged=True, cap_add=["SYS_RAWIO"], devices="/dev/gpiomem", command="python blinkt_red.py", detach=True)

    return str1 + str2 + "\n"

if __name__ == "__main__":
    app.run(host='0.0.0.0')