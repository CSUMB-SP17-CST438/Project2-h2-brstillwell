import os
import flask
import flask_socketio
import requests
import flask_sqlalchemy
import random
#from rfc3987 import parse
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

def chatbot_message(data):
    #print "this is to the damn chatbot"
    commands = data['text'].split(' ')
    if (commands[1] == "about"):
        message1 = models.ChatRoom("TomBot", "static/img/tom2.jpg", "Myspace is better")
        db.session.add(message1)
        db.session.commit()
        return "Myspace is better"
    elif (commands[1] == "help"):
        message1 = models.ChatRoom("TomBot", "static/img/tom2.jpg", "!! say: Make bot say something")
        message2 = models.ChatRoom("TomBot", "static/img/tom2.jpg", "!! about: Tells about the bot")
        message3 = models.ChatRoom("TomBot", "static/img/tom2.jpg", "!! weather: Gives current weather forecast")
        message4 = models.ChatRoom("TomBot", "static/img/tom2.jpg", "!! joke: Tells a joke")
        db.session.add_all([message1, message2, message3, message4])
        db.session.commit()
        return "help messages"
    elif (commands[1] == "say"):
        speak = ""
        for index in range(len(commands)):
            if index > 1:
                speak = speak + " " + commands[index];
        message1 = models.ChatRoom("TomBot", "static/img/tom2.jpg", speak)
        db.session.add(message1)
        db.session.commit()
        return speak
    elif (commands[1] == "weather"):
        response = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Marina&APPID=375a6ab765b60a9834b31204e67b8c08')
        json_body = response.json()
        message1 = models.ChatRoom("TomBot", "static/img/tom2.jpg", "Weather in Marina, CA: " + json_body['weather'][0]['description'])
        db.session.add(message1)
        db.session.commit()
        return "Weather in Marina, CA: pending"
    elif (commands[1] == "joke"):
        message1 = models.ChatRoom("TomBot", "static/img/tom2.jpg", "Today a man knocked on my door and asked for a small donation towards the local swimming pool. I gave him a glass of water.")
        db.session.add(message1)
        db.session.commit()
        return "Today a man knocked on my door and asked for a small donation towards the local swimming pool. I gave him a glass of water."
    else:
        message1 = models.ChatRoom("TomBot", "static/img/tom2.jpg", "Unrecognized command: " + data['text'])
        db.session.add(message1)
        db.session.commit()
        return "Unrecognized command: " + data['text']
        
    '''elif (commands[1] == "yoda"):
        yoda = ('thJ4GCpx5lmshJlFqLbRaXr5cb0Yp1SDDbRjsnDU0dJo1XRpZ5')
        parser = argparse.ArgumentParser(description='What do you want Yoda to say?')
        parser.add_argument( 'yodasLine', help='What do you want Yoda to say?' )
        args = parser.parse_args()
        
        str = urllib.quote(args.yodasLine)
        opener = urllib2.build_opener()
        opener.addheaders = [("X-Mashape-Authorization", yoda)]
        socket = opener.open('https://yoda.p.mashape.com/yoda?sentence=' +
        str)
        content = socket.read()
        socket.close()
        print content
        print ""
        print ""
        speak = ""
        for index in range(len(commands)):
            if index > 1:
                speak = speak + " " + commands[index];
        message1 = models.ChatRoom("TomBot", "static/img/tom2.jpg", speak)
        db.session.add(message1)
        db.session.commit()'''
    
@app.route('/')
def hello():
    return flask.render_template('index.html')
            

@socketio.on('connect')
def on_connect():
    socketio.emit('hello to client', {
        'message': 'Hey there!'
    })
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
    print data
    print ""
    if data['type'] == 'Bot':
        print "The Bot has received this"
        print ""
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
        else:
            response = requests.get(
                'https://www.googleapis.com/oauth2/v3/tokeninfo?id_token=' + data['google_user_token'])
            json = response.json()
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
    message = data['number'].split(" ")
    if (message[0] == "!!"):
        chatbot_message({'text': data['number']})
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

