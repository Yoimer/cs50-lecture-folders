# Project 2
### Web Programming with Python and JavaScript


## Flack, a Chat Application

This is a simple Flask web application where users can enter giving a name, and then both create Chatrooms called Channels or go into one of the already existing (in case there is already one at least).

Into a Channel, they can type and send messages which only exist into that Channel and other users can read them and response.


**Application.py**

After creating a Flask instance and configuring a couple of session parameters a SocketIO instance is created too. That make necessary change the usual app.run() at the bottom of the file for socketio.run(app).

The first view here is *index*. There are a couple of ´try´s in case the user close the tab and enter again to the app. In that case the application can be able to remember the name and also remember the last channel the user was in.


*name* takes care of the 'username' that is chosen in the first input, and it remember that name into session.


*lastChannel* is in charge to remember the last Channel the user visited and doesn't return anything.


*channel* is used to create new channels and store then into the global variable `channels` which is declared above. All channels are instances of a custom Class that I created in a separated file called *channels.py* so this class is able to store a name for the channel, and a list of dict, where every dict correspond to a message and contains the message itself, the name of the sender, the channel name (this is redundant) and the time when it was sent.

*delete* is just for deleting messages. The user choses the one she or he wants to delete and just that is removed with a pretty animation.

The last two views are socket relatives. The first is taking care of new messages, storing them into their correspondent Channel and then sending it back to the chatroom to be shown. It also stamp the time for that message before append it to the Channel.

Then the second socketio view is used when the user changes the channel. All available messages belonging to that channel are fetched and sent.

**Static**

Three images are stored here. Also the custom CSS stylesheet *styles.css* and *formName.js* which is used to manage the case when the user provides his or her name the first time that arrive on the webapp.

**Templates**

Finally in *templates* there are just two files. *layout.html* is used to establish a base template (just for good habit because in this app there is only one more template and isn't very helpful). There you can find all `rel` for stylessheets, the code for jquery, the socketio, and also the navbar.

In index there are many lines not just in HTML but also in JavaScript. There are severals forms, one for introduce the username, other for creating a new channel and the third for typing and sending messages.

Channel room is a `div`, within this div there is another `div` that contain an unordered list with `id` *chatMessages*. This is where all new messages are appended. At the end of the file we find the two big scripts with comments that help understand how the Channel name is provided and how messages are sent and received.

**Personal Touch**

My personal touch in this project was to implement the option of deleting your own messages. An X appear close to the message when hover with the pointer and the message disappears with a css animation. The message is removed from the database.
