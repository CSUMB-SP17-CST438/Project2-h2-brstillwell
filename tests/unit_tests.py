import unittest
import app
#import flask_testing, requests

class unit_testing(unittest.TestCase):
    def test_empty_string(self):
        result = ''.split()
        self.assertEquals(result, [])
        
class socketio_testing(unittest.TestCase):
    def test_server_sends_hello(self):
        client = app.socketio.test_client(app.app)
        r = client.get_received()
        # print r
        self.assertEquals(len(r), 4)
        from_server = r[0]
        self.assertEquals(
            from_server['name'], 
            'hello to client'
        )
        data = from_server['args'][0]
        self.assertEquals(data['message'], 'Hey there!')
        
    def test_server_relays_message(self):
        client = app.socketio.test_client(app.app)
        client.emit('new message', {
            'type': 'Bot',
            'name': 'test',
            'picture': 'test',
            'number': 'Potatoes are cool!'
        })
        r = client.get_received()
        # print r
        self.assertEquals(len(r), 7)
        from_server = r[1]
        self.assertEquals(
            from_server['name'],
            'usersCount'
        )
        data = from_server['args'][0]
        
        
if __name__ == '__main__':
    unittest.main()