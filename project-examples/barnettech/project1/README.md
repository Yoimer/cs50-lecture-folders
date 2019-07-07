# Project 1
# A website where folks can search for a zip code and find the weather info
# for that locale.  Then they can also checkin and leave a comment at that
# location page.

Web Programming with Python and JavaScript
1.)  First from the command line set the environment variables by typing
     source setenvars.sh, then start it up with flask run
2.)  The script import.py to load in the csv file is with the csv file
  being imported in the zips directory.

3.)  Ok lots of files to describe
  application.py has all of the program logic, routes, queries and such
  html files:  a.) layout.html gives an overall layout to the site, great so I only need
    to write the logout code once for instance. b.)  index.html is the main login page
    c.)  searchresults.html show the results after looking up a zipcode in the database
    d.)  location.html shows the location page for a given zipcode
    e.)  login.html is the destination the route login sends you upon loggging in or registering
    f.)  misc. files:  setenvars.sh sets the environment variables, connect_heroku.sh
         is there to easily connect to the heroku db.
    g.)  d42oslhd6lgnv4.sql is the db dump from heroku
