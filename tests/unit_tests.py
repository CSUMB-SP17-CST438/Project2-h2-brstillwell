import unittest
import app

class unit_testing(unittest.TestCase):
    def test_empty_string(self):
        result = ''.split()
        self.assertEquals(result, [])
        
class socketio_testing(unittest.TestCase):
    def test_server_relays_message(self):
        client = app.socketio.test_client(app.app)
        client.emit('new message', {
            'my message': 'Potatoes are cool!'
        })
        r = client.get_received()
        # print r
        self.assertEquals(len(r), 2)
        from_server = r[1]
        self.assertEquals(
            from_server['name'],
            'got your message'
        )
        data = from_server['args'][0]
        self.assertEquals(
            data['your message'],
            u'Potatoes are cool!'
        )
        
if __name__ == '__main__':
    unittest.main()