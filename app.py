import os
import flask
import flask_socketio
import requests
import flask_sqlalchemy
from flask import Flask, request

app = flask.Flask(__name__)
socketio = flask_socketio.SocketIO(app)
#all_numbers = [];
global all_users
all_users = [];
users = 0;

import models 

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:admin@localhost/postgres'
#app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')

db = flask_sqlalchemy.SQLAlchemy(app)


def usersOn():
    if users != None:
        if users >= 0:
            users = users + 1
    else:
        global users
        users = 1;
    print users
    countUser(users)
def usersOff():
    if users != None:
        if users >= 0:
            users = users - 1
    else:
        global users
        users = 0;
    print users
    countUser(users)
    
@app.route('/')
def hello():
    return flask.render_template('index.html')
            
    
def countUser(q):
    print "here to get the users = " + str(q)
    socketio.emit('usersCount', q)

@socketio.on('connect')
def on_connect():
    usersOn()
    chats = models.ChatRoom.query.all()
    currentUsers = models.Users.query.all()
    chatlog = []
    userlog = []
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
    usersOff()
    qusers = models.Users.query.all()
    userLeft = models.Users
    innactive = False
    for u in qusers:
        if u.id == request.sid:
            innactive = True
            userLeft = u
    if innactive == True:
        db.session.delete(userLeft)
        db.session.commit()
    print 'Someone disconnected!'

@socketio.on('new user')
def on_new_user(data):
    response = requests.get(
            'https://graph.facebook.com/v2.8/me?fields=id%2Cname%2Cpicture&access_token=' + data['facebook_user_token'])
    json = response.json()
    all_users.append({
         #'name': data['name'],
         #'picture': data['picture']
         'name': "TomBot",
         'picture': "static/img/tom2.jpg"
         })
    socketio.emit('userList', {
        'numbers': all_users
    })

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
            #sql = text("select * from users where user = '" + newUser.user + "'")
            #result = db.engine.execute(sql)
            #print "result = "
            #names = []
            #for row in result:
                #names.append(row[0])
            #db.session.add(newUser)
        else:
            response = requests.get(
                'https://www.googleapis.com/oauth2/v3/tokeninfo?id_token=' + data['google_user_token'])
            json = response.json()
            newRecord = models.ChatRoom(json['name'], json['picture'], data['number'])
            qusers = models.Users.query.all()
            innactive = False
            for u in qusers:
                if u.id == request.sid:
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
    
if __name__ == '__main__':
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )

