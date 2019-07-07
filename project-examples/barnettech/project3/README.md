# Project 3

Web Programming with Python and JavaScript

A django app showcasing a Pinocchios restaurant menu
for CS50 Web Programming with Python and JavaScript

## Getting Started

Spin up the app by typing in python manage.py runserver 0.0.0.0:8080
from within the project 3 folder, or run sh startserver.sh

FYI to test checkout with stripe API, which I integrated with to
checkout, using their payment gateway, here are a list of fake
credit cards to use https://stripe.com/docs/testing#cards
I've been using test visa number 4242 4242 4242 4242 which is on
this list for testing, any valid date in the future, and any
three digit value for the 3 digit code seems to work.


## File Listing
1.)  In the static directory you'll find index.css for some css rules
and index.js with all of the JavaScript code for the project
2.)  In the templates directory within the pinocchios folder
  you'll find all the html templates
  for the project, registration forms are in the registration folder,
  base_generic.html is the basic layout html file, then you have
  the existing-orders.html showing administrators the orders already
  in the system.  order_food_form.html is the template for ordering
  food.  signup.html is the registration form.  thankyou.html is the
  landing page for after checkout. menu.html shows the basic menu,
  without the ability to order from this page though.

  Within the orders folder, you'll find the admin.py file which registers
  all the admin pages.  apps.py lists your app names, forms.py has
  registration form data.  models.py has all your database models setup
  there.  The project did not ask for unit tests, but tests.py is where
  those would go.  urls.py has routing information and points to views.py
  for further definition of what is served up at each route.  In views.py
  you have all your controller / application logic, which will then be
  displayed in your templates (views -- classic MVC architecture).

