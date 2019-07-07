import os
import requests, json
import datetime

from flask import Flask, render_template, jsonify, request, session, abort
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_session import Session
from sqlalchemy import create_engine

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

#the homepage at index, serves up the page to login
@app.route("/")
def index():
    return(render_template("index.html", homepage=True))

#upon upon submittal of login credentials the route /login is invoked
@app.route("/login", methods=['GET', 'POST'])
def login():
  username = request.form.get("username")
  password = request.form.get("password")
  newusername = request.form.get("newusername")
  newpassword = request.form.get("newpassword")
  #check if the user is logged in to tailor the message returned
  if session['logged_in'] != True:
    if newusername != '' and newpassword != '':
      message="Wecome to the site, glad you were able to create an account!"
      session['logged_in'] = True
      session['username'] = newusername
      print(newusername)
      if newusername != None and newpassword != None:
        db.execute("INSERT INTO login (username, password) VALUES (:username, :password)",
          {"username": newusername, "password": newpassword})
    elif username != '' and password != '':
      # See if user exists.
      rowcount = db.execute("SELECT * FROM login WHERE username = :username and password = :password", {"username": username, "password": password}).rowcount
      if rowcount == 1:
        message="Welcome Back!"
        session['username'] = username
        session['logged_in'] = True
      elif rowcount == 0:
        message="No user found, please try logging in again or create an account"
        session['logged_in'] = False
  else:
      message='already logged in'
  # All done commit to database!
  db.commit()
  return(render_template("login.html", message=message))

#upon clicking logout this route is called
@app.route("/logout", methods=['GET', 'POST'])
def logout():
    session['logged_in'] = False
    return(render_template("index.html", homepage=True))

#this is the location page for any given zip code
@app.route("/location", methods=['GET', 'POST'])
def location():
    zipcode = request.args.get('zipcode')
    returned_zip_info = db.execute("SELECT * from locations WHERE zipcode = :zipcode", {"zipcode": zipcode}).fetchone()
    lat = float(returned_zip_info[4])
    long = float(returned_zip_info[5])
    # pass in a lat and long to get weather info from the darksky api
    thestring = f"https://api.darksky.net/forecast/34b6298c5f0fe67d3cc741bb29bb0e22/{lat},{long}"
    query = requests.get(thestring).json()
    currently = query["currently"]
    temp = query["currently"]["temperature"]
    humidity = query["currently"]["humidity"] * 100
    time = datetime.datetime.fromtimestamp(int(query["currently"]["time"])).strftime('%Y-%m-%d %H:%M:%S')
    #grab all the comments from checkins at this location
    location_comments = db.execute("SELECT * FROM checkin where zipcode = :zipcode", {"zipcode": zipcode}).fetchall()
    #see how many comments there are from checkins at this location
    already_commented_count = db.execute("SELECT count(*) FROM checkin where username = :username and zipcode = :zipcode", {"username" : session['username'], "zipcode" : zipcode}).fetchone()
    total_checked_in =  db.execute("SELECT count(*) FROM checkin where zipcode = :zipcode", {"zipcode" : zipcode}).fetchone()
    if already_commented_count[0] == 1:
        already_commented = True
    else:
        already_commented = False
    print(f"temp is {temp}")
    return(render_template("location.html", total_checked_in=total_checked_in[0], zipcode=zipcode, time=time, humidity=humidity, returned_zip_info=returned_zip_info, lat=lat, long=long, temp=temp, currently=currently, location_comments=location_comments, already_commented_count=already_commented_count, already_commented=already_commented ))

#this is the route called when a user submits that they are
#checking in at a given zip code
@app.route("/checkin", methods=['GET', 'POST'])
def checkin():
     print('got in here')
     yourusername = request.form.get("yourusername")
     comment = request.form.get("comment")
     zipcode = request.form.get("zipcode")
     already_commented_count = db.execute("SELECT count(*) FROM checkin where username = :username and zipcode = :zipcode", {"username" : session['username'], "zipcode" : zipcode}).fetchone()
     if already_commented_count[0] == 1:
        already_commented = True
     else:
        already_commented = False
     if already_commented_count[0] == 0:
       #if they havent checked in yet for this location, add their comment/checkin to the db
       db.execute("INSERT INTO checkin (zipcode, username, comment) VALUES (:zipcode, :username, :comment)", {"zipcode": zipcode, "username": yourusername, "comment": comment})
       already_commented = True
       db.commit()
     returned_zip_info = db.execute("SELECT * from locations WHERE zipcode = :zipcode", {"zipcode": zipcode}).fetchone()
     count_returned_zip_info = db.execute("SELECT count(*) from locations WHERE zipcode = :zipcode", {"zipcode": zipcode}).fetchone()
     if count_returned_zip_info[0] == 1:
       lat = float(returned_zip_info[4])
       long = float(returned_zip_info[5])
       #we're going to reshow the weather data after submittal of the checkin
       #so grab the weather data again
       thestring = f"https://api.darksky.net/forecast/34b6298c5f0fe67d3cc741bb29bb0e22/{lat},{long}"
       query = requests.get(thestring).json()
       currently = query["currently"]
       temp = query["currently"]["temperature"]
     else:
       lat = ""
       long = ""

     total_checked_in =  db.execute("SELECT count(*) FROM checkin where zipcode = :zipcode",
     {"zipcode" : zipcode}).fetchone()
     location_comments = db.execute("SELECT * FROM checkin where zipcode = :zipcode",
     {"zipcode": zipcode}).fetchall()
     return(render_template("location.html", currently=currently, total_checked_in=total_checked_in[0],
     zipcode=zipcode, returned_zip_info=returned_zip_info, lat=lat, long=long, temp=temp,
     location_comments=location_comments, already_commented_count=already_commented_count, already_commented=already_commented ))

#upon searching for a zipcode the results are shown after
#calling this route
@app.route("/searchresults", methods=['GET', 'POST'])
def searchresults():
    zipcode = request.form.get("zipcode")
    #grab all the search results from the zipcode search from the db, passing in zip
    returned_zip_info = db.execute("SELECT * from locations WHERE zipcode like :zipcode",
    {"zipcode": f"%{zipcode}%"}).fetchall()
    count_returned_zip_info = db.execute("SELECT count(*) from locations WHERE zipcode = :zipcode",
    {"zipcode": zipcode}).fetchone()
    if count_returned_zip_info[0] == 1:
      zipreturned = True
    else:
      zipreturned = False
      lat = ''
      long = ''
      returned_zip_info = 'That zipcode is not in our database'
    print(f"returned zipcode information is {returned_zip_info}")
    return(render_template("searchresults.html", count_returned_zip_info=count_returned_zip_info[0],
    returned_zip_info=returned_zip_info, zipcode=zipcode, zipreturned=zipreturned))

#this is an api url to get info in json format, passing in a zip
@app.route("/api/<string:zipcode>")
def zip_code(zipcode):
    """Return details about a zip code from the db."""
    #get info from the db on this zipcode
    returned_zip_info = db.execute("SELECT * from locations WHERE zipcode = :zipcode",
    {"zipcode": zipcode}).fetchone()
    count_returned_zip_info = db.execute("SELECT count(*) from locations WHERE zipcode = :zipcode",
    {"zipcode": zipcode}).fetchone()
    if count_returned_zip_info[0] < 1:
        return abort(404)
    #get all the info about the checkins at this locale
    checkins = db.execute("SELECT count(*) from checkin WHERE zipcode = :zipcode",
    {"zipcode": zipcode}).fetchone()
    #return 'the data is %s' % returned_zip_info
    #return the data in json format by jsonifying it
    return jsonify({
            "zip": returned_zip_info[1],
            "place name": returned_zip_info[2],
            "state": returned_zip_info[3],
            "latitude": str(returned_zip_info[4]),
            "longitude": str(returned_zip_info[5]),
            "population": returned_zip_info[6],
            "check_ins": checkins[0],
        })