# DevOpsR


1. Designed a simple "Hello World" application that exposes the following HTTP-based APIs:

First Request: PUT /hello/<username> { “dateOfBirth”: “YYYY-MM-DD” }
Second Request: Get /hello/<username>

Solution: To achieve this task, I am going to use python flask framework for exposing APIs (GET and PUT). I used multiple modules which is listed below.

## Requirements

| Name | Version |
|------|---------|
| tinydb | == 3.15.0 |
| Flask | == 0.12.2 |
| werkzeug | == 0.16.1 |
| flask-restplus | == 0.3.8 |
| Flask-AWSCognito |== 1.3 |
| Flask-RESTful | == 0.3.8 |
| flask-restful-swagger-2 | == 0.35 |

The Code is pretty simple and easy to understand. Here we will explain the code and will describe the steps to provision it on AWS Elastic Beanstalk Service in Dev and Prod Environment. For environment specific we create a load-balanced, scalable environment or a single-instance environment in Elastic Bean Stalk but here I am using Single-Instance for development and Load-balanced for Production Environment.


### AWS Elastic Beanstalk

It is possible to host commercial grade Flask application on AWS with EC2 instance. Launching EC2 instance is easy but resource management is an overhead. For better resource usage, Lambda and API Gateway is an alternative. But it comes with resource configuration overhead.

AWS Elastic Beanstalk (EB) reduces management complexity without restricting choice or control. All we need to do is upload the application and EB itself handles the details of:
1. Capacity provisioning
2. Load balancing
3. Scaling
4. Application health monitoring

## Inputs

1. `DockerFile`         - A Dockerfile is a text document that contains all the commands a user could call on the command line to assemble an image.
2. `app.py`             - Python file which consist logic to acheive the task.
3. `requirements.txt`   - we generate and share requirements. txt files to make it easier to install the correct versions of the required Python libraries (or “packages”) to run the Python code we have written.
4. `gitignore`          - The purpose of gitignore files is to ensure that certain files not tracked by Git remain untracked.
5. `Flask`              - a popular Python micro framework for the web

```
Prerequisites to Deploy a New Flask app on AWS Elastic Beanstalk
1. EB CLI
2. AWS Key and Secret
```

## steps
```
## To Initialize EB CLI repository with the eb init command
$ eb init -r ap-south-1 flask-rest-api

## (optional) Run eb init again to configure a default keypair so that you can connect to the EC2 instance running your application with SSH:
$ eb init
Do you want to set up SSH for your instances?
(y/n): y
Select a keypair.
1) my-keypair
2) [ Create new KeyPair ]

## To deploy in DEV Environment
$ eb create dev-flask-env --single -r ap-south-1

## To deploy in DEV Environment
$ eb create dev-flask-env -r ap-south-1

## Once Code is updated at my workstation then I can deploy in DEV environment by this command
$ eb deploy dev-flask-env

## After satisfaction that everything is working fine then we can deploy in Prod Environment
$ eb deploy prod-flask-env

## To Delete Environment
$ eb terminate dev-flask-env
$ eb terminate prod-flask-env
```

## Extras

Although there are multiple methods to Deploy on AWS Elastic Beanstalk to achieve this tasks which are mentioned below..

1. CI/CD pipeline for deployment
- Configuring CI/CD in your local system and CircleCI (or some other CI/CD tool), so that anytime you push your code to a Git repository, it will get automatically deployed to Beanstalk.

2. Making a source bundle of your application code manually zipping it in a file and uploading it to Elastic Beanstalk.

3. Using an already written script to make a zip file and uploading the same zip to Beanstalk. This is 95% similar to the first one, just saves you from the hassle of selecting multiple files and zipping them.

4. We can also create dockerized image and provision them on EKS/GCP as Pod with deployment strategy i.e. Blue-Green/Canary/Rollout strategies 

5. Any tests to check for success or failure of the pipeline.
- We can take help for flask-unittest which is developed by Python (https://pypi.org/). A hassle free solution to testing flask application using unittest. The goal is to make test code by using a unit testing framework.
- We can also use Docker Bench for Security for scanning the image and then upload it in private Repository (ECR/GCR)
