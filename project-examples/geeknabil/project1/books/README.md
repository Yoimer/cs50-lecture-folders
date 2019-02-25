# Project 1: book review website
it's a site that let users search for books, see reviews, add reviews and use it's api 


# import.py 
This file read about 5000 different book from books.csv file and import them in Postgresql


# application.py
This file includes all web application's logic btw handling user requests, calling Goodreads API and dealing with DB.

There are routes that let users:

1- register with validating user inputs.

2- login also with validation and remembering users by storing their sessions.

3- logout.

4- search for their favourite book with handling possible search queries and matching errors.

5- see information about selected book.

6- add review and only one review.

7- see added reviews submitted by other users.

8- see book rate and it's average review from Goodreads.

9- use site api via (/api/isbn) will provide info for book isbn, title, author, pupublication year and reviews.


# Usage 
You can either clone this repo and run it if you have flask server running

or visit http://ide50-mohamed-nabil.cs50.io:8080/ with knowing that it's not always be running on cloud9 server

if down, you can contact me personally to run the server. 

I know this isn't a funny game so I will update this section when deploying to permanint server.
