import os
import flask
import flask_socketio
import requests
import flask_sqlalchemy
import random
from rfc3987 import parse
from flask import Flask, request

app = flask.Flask(__name__)
socketio = flask_socketio.SocketIO(app)
#all_numbers = [];
global all_users
all_users = [];
all_connected_users = { };

import models 

#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:admin@localhost/postgres'
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')

db = flask_sqlalchemy.SQLAlchemy(app)

    
@app.route('/')
def hello():
    return flask.render_template('index.html')
            

@socketio.on('connect')
def on_connect():
    #socketio.emit('hello to client', {
    #    'message': 'Hey there!'
    #})
    #print "new method" + socketio.clientsCount
    chats = models.ChatRoom.query.all()
    currentUsers = models.Users.query.all()
    chatlog = []
    userlog = []
    name = random.randrange(1000, 9999)
    all_connected_users[flask.request.sid] = name
    socketio.emit('usersCount', len(all_connected_users))
    for c in chats:
        chatlog.append({
            'name': c.user,
            'picture': c.image,
            'number': c.message
            })
    for u in currentUsers:
        userlog.append({
            'name': u.user,
            'picture': u.image
        })
    socketio.emit('userList', {
        'numbers': userlog
    })
    socketio.emit('chatroom', {
        'numbers': chatlog
    })
    print 'Someone connected!'
    

@socketio.on('disconnect')
def on_disconnect():
    qusers = models.Users.query.all()
    userLeft = models.Users
    del all_connected_users[flask.request.sid]
    socketio.emit('usersCount', len(all_connected_users))
    innactive = False
    for u in qusers:
        if u.id == request.sid:
            innactive = True
            userLeft = u
    if innactive == True:
        db.session.delete(userLeft)
        db.session.commit()
    print 'Someone disconnected!'

@socketio.on('new message')
def on_new_number(data):
    if data['type'] == 'Bot':
        newRecord = models.ChatRoom(data['name'], data['picture'], data['number'])
        db.session.add(newRecord)
        db.session.commit()
    elif data['type'] == 'weather':
        response = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Marina&APPID=375a6ab765b60a9834b31204e67b8c08')
        json_body = response.json()
        newRecord = models.ChatRoom(data['name'], data['picture'], "Weather in Marina, CA: " + json_body['weather'][0]['description'])
        db.session.add(newRecord)
        db.session.commit()
    else:
        if data['type'] == "facebook":
            response = requests.get(
                'https://graph.facebook.com/v2.8/me?fields=id%2Cname%2Cpicture&access_token=' + data['facebook_user_token'])
            json = response.json()
            print "wtf" 
            print data['number'][0] 
            if data['number'][0] == 'h':
                web = parse(data['number'], rule='IRI')
                print "This is the repsonse: ", web
            print ""
            print ""
            newRecord = models.ChatRoom(json['name'], json['picture']['data']['url'], data['number'])
            print('Client connected', request.sid)
            qusers = models.Users.query.all()
            innactive = False
            for u in qusers:
                if u.id == request.sid:
                    innactive = True
            if innactive == False:
                newUser = models.Users(newRecord.user, newRecord.image, request.sid)
                db.session.add(newUser)
        else:
            response = requests.get(
                'https://www.googleapis.com/oauth2/v3/tokeninfo?id_token=' + data['google_user_token'])
            json = response.json()
            print "wtf" 
            print data['number'][0] 
            if data['number'][0] == 'h':
                web = parse(data['number'], rule='IRI')
                print "This is the repsonse: ", web
            print ""
            print ""
            newRecord = models.ChatRoom(json['name'], json['picture'], data['number'])
            qusers = models.Users.query.all()
            innactive = False
            for u in qusers:
                if u.image == newRecord.image:
                    innactive = True
            if innactive == False:
                newUser = models.Users(newRecord.user, newRecord.image, request.sid)
                db.session.add(newUser)
        db.session.add(newRecord)
        db.session.commit()
    chats = models.ChatRoom.query.all()
    users = models.Users.query.all()
    chatlog = []
    userlog = []
    for c in chats:
        chatlog.append({
            'name': c.user,
            'picture': c.image,
            'number': c.message
            })
    for u in users:
        userlog.append({
            'name': u.user,
            'picture': u.image
            })
    socketio.emit('userList', {
        'numbers': userlog
    })
    socketio.emit('chatroom', {
        'numbers': chatlog
    })
    socketio.emit('got your message', {
        'your message': data['number']
    })
    
if __name__ == '__main__':
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )

