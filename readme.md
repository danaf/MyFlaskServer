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

EC2 Instance: Build and tag for AWS ECR, and then push into ECR – this was for public
    docker build -t mypython-docker .

    docker tag mypython-docker:latest public.ecr.aws/x1p1r6n9/my-flask-repo:latest

    docker push public.ecr.aws/x1p1r6n9/my-flask-repo:latest

EC2 Public:

    docker build -t saladprivate .

    docker tag saladprivate:latest 339712819389.dkr.ecr.us-east-1.amazonaws.com/saladprivate:latest

    docker push 339712819389.dkr.ecr.us-east-1.amazonaws.com/saladprivate:latest

EC2 Private (second attempte; first was private) 
* https://us-east-1.console.aws.amazon.com/ecr/repositories/private/339712819389/saladprivate?region=us-east-1

* Click view push commands to get the four push commands


********************
Run Docker Image as a Container
********************
docker build -t mypython-docker .

docker run mypython-docker

Use this to run locally; make calls in client file to http://127.0.0.1:5000/login:
docker run -d -p 5000:5000 mypython-docker

Without Detach:
docker run -p 5000:5000 mypython-docker



docker run saladprivate

Use this to run locally; make calls in client file to http://127.0.0.1:5000/login:
docker run -d -p 5000:5000 saladprivate

Without Detach:
docker run -d -p 5000:5000 saladprivate



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
https://stackoverflow.com/questions/17818485/flask-web-app-not-responding-to-external-requests-on-ec2 <-- info about not responding on 5000


********************
AWS Services – Steve suggests AWS App Runner
********************
https://docs.aws.amazon.com/decision-guides/latest/containers-on-aws-how-to-choose/choosing-aws-container-service.html

AWS App Runner Container Deployment:
https://docs.aws.amazon.com/app2container/latest/UserGuide/a2c-integrations-apprunner.html

********************
My Flask Server GitHub Repo
(danaf@essentialinstructions account)
********************
https://github.com/danaf/MyFlaskServer

git clone https://github.com/danaf/MyFlaskServer.git
git pull https://github.com/danaf/MyFlaskServer.git


********************
AWS
********************

Configure
    AWS Access Key ID: key1
    AWS Secret Access Key: secretkey1
    Default Region: US
    Default output format: <none>


EC2 
    * Second New Instance Name: MyDebFServer (Debian-based)
    * Instance Name: My Flask Server
    * Instance Key Pair Name: Dana (See Dana.pem)

    Had to run followoing for SSH: chmod 0400 Dana.pem

    Log into EC2 in terminal:

    * cd /Users/dana/Downloads/MyFlaskServer
    * sudo ssh -i Dana.pem admin@ec2-18-216-162-56.us-east-2.compute.amazonaws.com


ECS
    * Cluster name – third attemp (second one is gone): FlaskCluster
    * Cluster name – second attempt: MyFCluster
    * Cluster name – first attempt: MyFlaskCluster (failed to create with some internal error)


ECR
    * Repo name: my-flask-repo

    Log in to ECR:
    aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws/x1p1r6n9






