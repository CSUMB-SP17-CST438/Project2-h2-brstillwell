import unittest
import app
from flask import Flask
import urllib2
import flask_testing, requests

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
        
    def test_bot_command_hidden(self):
        response = app.chatbot_message({'text': "!! hidden testing"})
        self.assertEquals(response, " testing")
    
    def test_bot_command_wrong(self):
        response = app.chatbot_message({'text': "!! test"})
        self.assertEquals(response, "Unrecognized command: !! test")
        
    def test_bot_command_none(self):
        response = app.chatbot_message({'text': "!!"})
        self.assertEquals(response, "Please specify command after '!!'")
    
    def test_bot_command_joke(self):
        response = app.chatbot_message({'text': "!! joke"})
        self.assertEquals(response, "Today a man knocked on my door and asked for a small donation towards the local swimming pool. I gave him a glass of water.")
        
    def test_bot_command_yoda(self):
        response = app.chatbot_message({'text': "!! yoda i hope you are having a wonderful day"})
        self.assertEquals(response, "Yoda translation success")
        
    def test_bot_command_yoda_bad(self):
        response = app.chatbot_message({'text': "!! yoda"})
        self.assertEquals(response, "Enter string after yoda command")
    
    
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
'''   

from flask_testing import TestCase

from app import db

class MyTest(TestCase):

    SQLALCHEMY_DATABASE_URI = "sqlite://"
    TESTING = True

    def create_app(self):
        # pass in test configuration
        return app.app

    def setUp(self):
        db.create_all()
        
    def test_something(self):
        user = User()
        db.session.add(user)
        db.session.commit()
        # this works
        assert user in db.session
        print "this is user: " + user
        response = self.client.get("/")

        # this raises an AssertionError
        assert user in db.session

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class MyTest(flask_testing.LiveServerTestCase):

    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        # Default port is 5000
        app.config['LIVESERVER_PORT'] = 8943
        # Default timeout is 5 seconds
        app.config['LIVESERVER_TIMEOUT'] = 10
        return app

    #def test_server_is_up_and_running(self):
        #response = urllib2.urlopen(self.get_server_url())
        #self.assertEqual(response.code, 200)
'''
if __name__ == '__main__':
    unittest.main()