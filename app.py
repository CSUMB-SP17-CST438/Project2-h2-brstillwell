import os
import flask
import flask_socketio

app = flask.Flask(__name__)
socketio = flask_socketio.SocketIO(app)

@app.route('/')
def hello():
    return flask.render_template('index.html')

@socketio.on('connect')
def on_connect():
    print 'Someone connected!'

@socketio.on('disconnect')
def on_disconnect():
    print 'Someone disconnected!'

all_numbers = [];
all_users = [];
@socketio.on('new message')
def on_new_number(data):
    all_numbers.append(data['number'])
    all_users.append(data['username'])
    socketio.emit('chatroom', {
        'numbers': all_numbers,
        'username': all_users
    })
if __name__ == '__main__':
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )

