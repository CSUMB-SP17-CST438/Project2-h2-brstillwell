import os
import flask
import flask_socketio
import requests

app = flask.Flask(__name__)
socketio = flask_socketio.SocketIO(app)
all_numbers = [];

@app.route('/')
def hello():
    return flask.render_template('index.html')
            

@socketio.on('connect')
def on_connect():
    print 'Someone connected!'

@socketio.on('disconnect')
def on_disconnect():
    print 'Someone disconnected!'


@socketio.on('new message')
def on_new_number(data):
    print "bout to get data"
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
        print "json requests made"
        all_numbers.append({
             'name': json['name'],
             'picture': json['picture']['data']['url'],
             'number': data['number']
             })
    #all_users.append(data['username'])
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

