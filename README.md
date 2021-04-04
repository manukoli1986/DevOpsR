# DevOpsR

1. Designed a simple "Hello World" application that exposes the following HTTP-based APIs:
Description: Saves/updates the given user’s name and date of birth in the database.
Request: PUT /hello/<username> { “dateOfBirth”: “YYYY-MM-DD” }
Response: 204 No Content
Note:
<username> must contain only letters.
YYYY-MM-DD must be a date before the today date.
Description: Returns hello birthday message for the given user

Request: Get /hello/<username>
Response: 200 OK
Response Examples:
A. If username’s birthday is in N days:
{ “message”: “Hello, <username>! Your birthday is in N day(s)”
}
B. If username’s birthday is today:
{ “message”: “Hello, <username>! Happy birthday!” }
Note: Use storage/database of your choice.




2. Produce a system diagram of your solution deployed to either AWS or GCP (it's not
required to support both cloud platforms).


It is possible to host commercial grade Flask application on AWS with EC2 instance. Launching EC2 instance is easy but resource management is an overhead. For better resource usage, Lambda and API Gateway is an alternative. But it comes with resource configuration overhead.

AWS Elastic Beanstalk (EB) reduces management complexity without restricting choice or control. All we need to do is upload the application and EB itself handles the details of:
Capacity provisioning
Load balancing
Scaling
Application health monitoring

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


