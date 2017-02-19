import os
import flask
import flask_socketio
import requests

app = flask.Flask(__name__)
socketio = flask_socketio.SocketIO(app)
all_numbers = [];
all_users = [];
users = 0;

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
    global something
    something = 0
    if something == 0:
        socketio.emit('chatroom', {
        'numbers': all_numbers
    })
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
        all_numbers.append({
         'name': data['name'],
         'picture': data['picture'],
         'number': data['number']
         })
    else:
        response = requests.get(
            'https://graph.facebook.com/v2.8/me?fields=id%2Cname%2Cpicture&access_token=' + data['facebook_user_token'])
        json = response.json()
        all_numbers.append({
             'name': json['name'],
             'picture': json['picture']['data']['url'],
             'number': data['number']
             })
    socketio.emit('chatroom', {
        'numbers': all_numbers
    })
    
if __name__ == '__main__':
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )

