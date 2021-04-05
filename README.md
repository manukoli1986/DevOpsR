# DevOpsR

1. Designed a simple "Hello World" application that exposes the following HTTP-based APIs:

First Request: PUT /hello/<username> { “dateOfBirth”: “YYYY-MM-DD” }
Second Request: Get /hello/<username>

Solution: To achieve this task, I am going to use python flask framework for exposing APIs (GET and PUT). I used multiple modules which is listed below.

```
tinydb==3.15.0
Flask==0.12.2
werkzeug==0.16.1
flask-restplus==0.13.0
Flask-AWSCognito==1.3
Flask-RESTful==0.3.8
flask-restful-swagger-2==0.35
```
The Code is pretty simple and easy to understand. Here we will explain the code sequential wise and will mention the steps to provision it on AWS Elastic Beanstalk Services. Although there are multiple ways to achieve this tasks which are mentioned below but I will use my method which I use to deploy in Dev and Prod Environment. 

```
AWS Elastic Beanstalk
```
It is possible to host commercial grade Flask application on AWS with EC2 instance. Launching EC2 instance is easy but resource management is an overhead. For better resource usage, Lambda and API Gateway is an alternative. But it comes with resource configuration overhead.

AWS Elastic Beanstalk (EB) reduces management complexity without restricting choice or control. All we need to do is upload the application and EB itself handles the details of:
Capacity provisioning
Load balancing
Scaling
Application health monitoring


```
Implementation Steps:w
```



2. Produce a system diagram of your solution deployed to either AWS or GCP (it's not
required to support both cloud platforms).



a) Making a source bundle of your application code manually zipping it in a file and uploading it to Elastic Beanstalk.
b) Using an already written script to make a zip file and uploading the same zip to Beanstalk. This is 95% similar to the first one, just saves you from the hassle of selecting multiple files and zipping them.
c) Using the AWS Elastic Beanstalk CLI(command line interface to directly deploy from your local system)
d) Configuring CI/CD in your local system and CircleCI (or some other CI/CD tool), so that anytime you push your code to a Git repository, it will get automatically deployed to Beanstalk.



3. Write configuration scripts for building and no-downtime production deployment of
this application, keeping in mind aspects that an SRE would have to consider.



Request 	Purpose
 GET        The most common method. A GET message is send, and the server returns data
 POST	    Used to send HTML form data to the server. The data received by the POST method is not cached by the server.
 HEAD	    Same as GET method, but no response body.
 PUT	    Replace all current representations of the target resource with uploaded content.
 DELETE	    Deletes all current representations of the target resource given by the URL.



 ################################


