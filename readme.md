********************
How to run my app in venv:
********************
cd /Users/dana/Downloads/myflaskproject
cd /Users/dana/Downloads/MyFlaskServer 

. .venv/bin/activate

flask --app hello run --debug


********************
Build Docker Image
********************
sudo docker build --tag mypython-docker .


********************
Run Docker Image as a Container
********************
docker run mypython-docker

Use this to run locally; make calls in client file to http://127.0.0.1:5000/login:
docker run -d -p 5000:5000 mypython-docker

Without Detach:
docker run -d -p 5000:5000 mypython-docker

********************
Commands
********************
docker image ls


********************
Fix Credentials Bug
********************
Had to change credsStore to credStore in (Users/Dana) ~/.docker/config.json


********************
Client
********************
See myclient/index.html



********************
Flask Cors
********************
Had to re-run with:
pip3 install Flask-Cors


********************
Tutorials:
********************
https://flask.palletsprojects.com/en/3.0.x/installation/
https://flask.palletsprojects.com/en/3.0.x/quickstart/
https://www.freecodecamp.org/news/how-to-dockerize-a-flask-app/
https://www2.cs.sfu.ca/CourseCentral/120/alavergn/Python_Instructions_MACOS.pdf
https://muditmathur121.medium.com/project-deploy-flask-app-using-ecs-ecr-6b804df1b524   <---


********************
AWS Services – Steve suggests AWS App Runner
********************
https://docs.aws.amazon.com/decision-guides/latest/containers-on-aws-how-to-choose/choosing-aws-container-service.html

AWS App Runner Container Deployment:
https://docs.aws.amazon.com/app2container/latest/UserGuide/a2c-integrations-apprunner.html


********************
AWS
********************
EC2 
    * Second New Instance Name: MyDebFServer (Debian-based)
    * Instance Name: My Flask Server
    * Instance Key Pair Name: Dana (See Dana.pem)

    Had to run followoing for SSH: chmod 0400 Dana.pem

    Log into EC2 in terminal:

    * cd /Users/dana/Downloads/MyFlaskServer
    * sudo ssh -i Dana.pem ec2-18-224-139-95.us-east-2.compute.amazonaws.com
    * ssh -i Dana.pem ec2-user@ec2-18-224-139-95.us-east-2.compute.amazonaws.com


    * sudo ssh -i Dana.pem ec2-18-216-162-56.us-east-2.compute.amazonaws.com
    * sudo ssh -i Dana.pem admin@ec2-18-216-162-56.us-east-2.compute.amazonaws.com


ECS
    * Cluster name – second attempt: MyFCluster
    * Cluster name – first attempt: MyFlaskCluster (failed to create with some internal error)

ECR
    * Repo name: my-flask-repo







