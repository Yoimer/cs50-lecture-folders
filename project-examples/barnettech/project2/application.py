import os
import requests

from flask import Flask, json, jsonify, render_template, request, session
from flask_session import Session
from flask_socketio import SocketIO, emit

#initialize to use socket.io
app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# list of chat rooms
channel_list = [['Lobby']]
# list of list, messages in each given chat room
chats_in_rooms = [['Lobby', 'Welcome!', 'To the lobby']]
# list of persons in each given chat room
persons_in_rooms = [['Lobby']]

#render the one page up, and start things up
@app.route("/")
def index():
    return(render_template("index.html", user_current_room=0, channel_list=channel_list, chats_in_rooms=chats_in_rooms, number_of_chats=len(channel_list)))

#upon chat emit process the chat to all users in the chatarena
@socketio.on("chat emit")
def chat(data):
    chattext = data["chattext"]
    #make sure this is an integer for use on the next line.
    room_number = int(data["channel_number"])
    #get rid of any white space to the right that may have been entered.
    chats_in_rooms[room_number].append(chattext.rstrip())
    #only keep 100 chats in the chat history
    if len(chats_in_rooms[room_number]) > 100:
      chats_in_rooms[room_number].pop(0)
    emit("chat emit", {'chattext': chattext, 'channel_number' : room_number},
      broadcast=True)

#upon submitting a chat channel, spin up a new channgle
@socketio.on("add channel")
def addchannel(data):
    newchannel = data["newchannel"]
    channel_list[0].append(newchannel)
    y = [newchannel, "Welcome"]
    #add the room to the list
    chats_in_rooms.append(y)
    emit("new channel", newchannel, broadcast=True)

#allows users to change the chat channel, and returns said chats for that room
@socketio.on("change channel")
def changechannel(data):
    #takes in the channel number (corresponds to list number)
    #to access data from the list
    channel_number = int(data["channel_number"])
    chats_in_this_room = chats_in_rooms[channel_number]
    #turn our list in a string readable by JavaScript
    chats_in_room = '<br>'.join(chats_in_this_room)
    emit("change channel", chats_in_room, broadcast=True)

#code to fly around the asteroids style spaceship circa 1979 / Atari 2600
@socketio.on("on fly")
def onfly(data):
    keyD = int(data["keyD"])
    keyS = int(data["keyS"])
    keyA = int(data["keyA"])
    keyW = int(data["keyW"])
    #broadcast which keys (AWSD) were pressed to move the ship on everyone's screen
    emit("on fly", {'keyD':keyD, 'keyS':keyS, 'keyA':keyA, 'keyW':keyW}, broadcast=True)