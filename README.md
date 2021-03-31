# DevOpsR

1. Design and code a simple "Hello World" application that exposes the following
HTTP-based APIs:
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


3. Write configuration scripts for building and no-downtime production deployment of
this application, keeping in mind aspects that an SRE would have to consider.



Request 	Purpose
 GET        The most common method. A GET message is send, and the server returns data
 POST	    Used to send HTML form data to the server. The data received by the POST method is not cached by the server.
 HEAD	    Same as GET method, but no response body.
 PUT	    Replace all current representations of the target resource with uploaded content.
 DELETE	    Deletes all current representations of the target resource given by the URL.