import unittest
import app
#import flask_testing, requests

class unit_testing(unittest.TestCase):
    def test_empty_string(self):
        result = ''.split()
        self.assertEquals(result, [])
        
    def test_bot_command_help(self):
        response = app.chatbot_message({'text': "!! help"})
        self.assertEquals(response, "help messages")
        
    def test_bot_command_about(self):
        response = app.chatbot_message({'text': "!! about"})
        self.assertEquals(response, "Myspace is better")
    
    def test_bot_command_weather(self):
        response = app.chatbot_message({'text': "!! weather"})
        self.assertEquals(response, "Weather in Marina, CA: pending")
    
    def test_bot_command_say(self):
        response = app.chatbot_message({'text': "!! say testing"})
        self.assertEquals(response, " testing")
    
    def test_bot_command_wrong(self):
        response = app.chatbot_message({'text': "!! test"})
        self.assertEquals(response, "Unrecognized command: !! test")
    
    def test_bot_command_joke(self):
        response = app.chatbot_message({'text': "!! joke"})
        self.assertEquals(response, "Today a man knocked on my door and asked for a small donation towards the local swimming pool. I gave him a glass of water.")
    
'''    def test_bot_command_help(self):
        response = app.chatbot_message({'text': "!! help"})
        self.assertEquals(response, "help messages")
    
    def test_bot_command_help(self):
        response = app.chatbot_message({'text': "!! help"})
        self.assertEquals(response, "help messages")
    
    def test_bot_command_help(self):
        response = app.chatbot_message({'text': "!! help"})
        self.assertEquals(response, "help messages")
    
    def test_bot_command_help(self):
        response = app.chatbot_message({'text': "!! help"})
        self.assertEquals(response, "help messages")
'''        
        
#class socketio_testing(unittest.TestCase):
#    def test_server_sends_hello(self):
#        client = app.socketio.test_client(app.app)
#        r = client.get_received()
#        # print r
#        self.assertEquals(len(r), 3)
'''        from_server = r[0]
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
        self.assertEquals(len(r), 6)
        from_server = r[1]
        self.assertEquals(
            from_server['name'],
            'usersCount'
        )
        data = from_server['args'][0]
  '''      
        
if __name__ == '__main__':
    unittest.main()