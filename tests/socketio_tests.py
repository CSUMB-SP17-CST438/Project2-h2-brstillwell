import unittest
import app
from flask import Flask
import urllib2
import flask_testing, requests



class socketio_testing(unittest.TestCase):
    def test_userlist(self):
        client = app.socketio.test_client(app.app)
        userlog = []
        userlog.append({
                'name': 'test1',
                'picture': 'static/img/testBot.png'
                })
        userlog.append({
                'name': 'test2',
                'picture': 'static/img/testBot.png'
                })
        client.emit('userList', {
            'numbers': userlog
        })
        received = client.get_received()
        print received
        client.disconnect()
        
    def test_chatroom(self):
        client = app.socketio.test_client(app.app)
        chatlog = []
        chatlog.append({
                'name': 'test1',
                'picture': 'static/img/testBot.png',
                'number': 'this is the first test'
                })
        chatlog.append({
                'name': 'test2',
                'picture': 'static/img/testBot.png',
                'number': 'this is the second test'
                })
        client.emit('chatroom', {
            'numbers': chatlog
        })
        received = client.get_received()
        client.disconnect()
        
class socketio_testing2(unittest.TestCase):
    def test_server_relays_message(self):
        client = app.socketio.test_client(app.app)
        client.emit('new message', {
            'type': 'Bot',
            'name': 'testBot',
            'picture': 'static/img/testBot.png',
            'number': 'Potatoes are cool!'
        })
        r = client.get_received()
        from_server = r[1]
        self.assertEquals(r[-1]['name'], "got your message")
        client.disconnect()
        
    def test_connect(self):
        client = app.socketio.test_client(app.app)
        received = client.get_received()
        self.assertEqual(len(received), 4)
        #print received[0]['args'][0]['message']
        self.assertEqual(received[0]['args'][0]['message'], 'Hey there!')
        client.disconnect()
        
    def test_disconnect(self):
        client = app.socketio.test_client(app.app)
        client.disconnect()
        received = client.get_received()
        self.assertEqual(received[-1]['args'][0]['message'], 'Bye!')
        
    
    
        

if __name__ == '__main__':
    unittest.main()