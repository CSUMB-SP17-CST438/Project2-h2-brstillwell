import os
import flask
import flask_socketio
import requests
import flask_sqlalchemy

app = flask.Flask(__name__)
socketio = flask_socketio.SocketIO(app)
#all_numbers = [];
all_users = [];
users = 0;

import models 

#URI scheme: postgresql://<username>:<password>@<hostname>:<port>/<database-name>
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:admin@localhost/postgres'
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
db = flask_sqlalchemy.SQLAlchemy(app)


def usersOn():
    if users != None:
        if users >= 0:
            users = users + 1
    else:
        global users
        users = 1;
    print users
def usersOff():
    if users != None:
        if users >= 0:
            users = users - 1
    else:
        global users
        users = 0;
    print users
    
@app.route('/')
def hello():
    return flask.render_template('index.html')
            
@app.route('/chatroom')
def chat():
    return flask.render_template('index.html')
    
socketio.on('getUsers')
def countUser():
    socketio.emit('usersCount', users)

@socketio.on('connect')
def on_connect():
    usersOn()
    print 'Someone connected!'

@socketio.on('disconnect')
def on_disconnect():
    usersOff()
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
         'picture': "static/tom2.jpg"
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
    else:
        response = requests.get(
            'https://graph.facebook.com/v2.8/me?fields=id%2Cname%2Cpicture&access_token=' + data['facebook_user_token'])
        json = response.json()
        newRecord = models.ChatRoom(json['name'], json['picture']['data']['url'], data['number'])
        db.session.add(newRecord)
        db.session.commit()
    chats = models.ChatRoom.query.all()
    chatlog = []
    for c in chats:
        chatlog.append({
            'name': c.user,
            'picture': c.image,
            'number': c.message
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

