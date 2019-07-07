# Project 3

Web Programming with Python and JavaScript

A django app showcasing a Django App with a ThreeJS game
for CS50 Web Programming with Python and JavaScript

Move the player around the screen (the blue box), and use the AWSD
keys to avoid the purple boxes, aliens or asteroids, we're not really
sure which, but they are deadly dangerous we are quite sure.

## Getting Started

Spin up the app by typing in python manage.py runserver 0.0.0.0:8080
from within the finalproject folder, or run sh startserver.sh

Create a login by clicking the register link.  Then login, and click on
the "Play Game" link within the left hand navigation.


## File Listing
1.)  In the static directory you'll find index.css for some css rules
and main.js, the primary javascript file with all of the JavaScript code for the project.
The player.js file spawns and controls the main player of the game.  alien.js spawns
and controls the aliens or asteroids the player is set on avoiding, because they
will cause sudden death and the end of the game.  three.min.js is the ThreeJS
library, which allows us to create 3d graphics.

2.)  In the templates directory within the retrogaming folder
  you'll find all the html templates
  for the project, registration forms are in the registration folder,
  base_generic.html is the basic layout html file, then you have
  the highscores.html showing highscores for the game.  signup.html
  is the registration form.  JSgame.html is the main template for the
  JavaScript game.  The settings.py file has all the basic django
  settings, to wire things up.

3.)  Within the asteroids folder, you'll find the admin.py file which registers
  all the admin pages.  apps.py lists your app names, forms.py has
  registration form data.  models.py has the database model for highscores
  setup there.  The project did not ask for unit tests, but tests.py is where
  those would go.  urls.py has routing information and points to views.py
  for further definition of what is served up at each route.  In views.py
  you have all your controller / application logic, which will then be
  displayed in your templates (views -- classic MVC architecture).

