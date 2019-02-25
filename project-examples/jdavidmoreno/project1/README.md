# Project 1
### Web Programming with Python and JavaScript

## NiceBooks Application

This is a simple Flask application thought to leave users register themselves and then be able to search, comment and leave rates to the available books.

Let's see part by part.

**application.py**

Here are the views. *Index* takes care of render the main page, at the same time try to remember the username before rendering.

*register*, *login* and *logout* are the basic views for managing user in the app.

In the client side, an user can type some words to search for books. Then in the *search* view a SQL request is executed looking for book with title or name or isbn like the word or word provided by the user and fetch a maximum of 10 entries. Then that data is rendered in  'search.html'.

In *book*, all relative to comments and rates is managed. It's only possible to leave a comment per book per user. More than one comment will end in a error message and nothing will be done. After the user comments or also if the user didn't comment this view will render a view of the book, with all the information available along with other users comments and its actual global rate.

Finally in *api* there is a mechanism to accept external request which will include a isbn number. With this isbn number this application will request to the database for this number and will return the data for that book. If no entrance is found it will raise a 404 error.

**static**

No so much here. Just a custom stylesheet that will complete that of Bootstrap.

**templates**

*layout.html* is the basic html for all the other templates. Here is written the head, and a piece of the body, that for the nav, as well as the script demanded by Bootstrap.

*index.html*, with some external images and able to say hello to the user by his or her name. The important here is the link to the search section.

In *search.html* users can look for book typing authors, titles or isbn. Database is asked for entries like those given by the user. The resultant books are enumerated as `li` elements.

Then when one of those `li` elements are clicked, the user is brought to *book.html*. A template that will show all data relative to that single book, including all comments made to it and the rates. Here it's also possible for the user to leave a comment and give the book a rate from 0 t0 5s.

*login.html* and *register.html* are made just for that, register and log in the web.

**import.py**

The last file is *import.py*, where a function has been implemented in order to load all data from *books.csv* to the chosen database scheme. This function works separately from the web application and can be called typing in the terminal 'python import.py'.
