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
        repsonse = app.chatbot_message({'text': "!! yoda i hope you are having a wonderful day"})
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
class ServerIntegrationTestCase(flask_testing.LiveServerTestCase):
    def create_app(self):
        return app.app
        
    def test_server_sends_hello(self):
        r = requests.get(self.get_server_url())
        self.assertEquals(r.text, '<html>\n    <head>\n        <link rel="stylesheet" type="text/css" href="/static/style.css" />\n\n        <meta\n             name="google-signin-scope"\n             content="profile email" />\n             <meta\n             name="google-signin-client_id"\n             content="233732937185-vs8j3hes4a27uf6ufvhq7peijbbr6tub.apps.googleusercontent.com" />\n         <script src="https://apis.google.com/js/platform.js" async defer>\n         </script>\n    \n        <script>\n              window.fbAsyncInit = function() {\n                FB.init({\n                  appId      : \'390393557996792\',\n                  xfbml      : true,\n                  version    : \'v2.8\'\n                });\n                FB.AppEvents.logPageView();\n              };\n            \n              (function(d, s, id){\n                 var js, fjs = d.getElementsByTagName(s)[0];\n                 if (d.getElementById(id)) {return;}\n                 js = d.createElement(s); js.id = id;\n                 js.src = "//connect.facebook.net/en_US/sdk.js";\n                 fjs.parentNode.insertBefore(js, fjs);\n               }(document, \'script\', \'facebook-jssdk\'));\n               \n               function testAPI() {\n                console.log(\'Welcome!  Fetching your information.... \');\n                FB.api(\'/me\', function(response) {\n                  console.log(\'Successful login for: \' + response.name);\n                  document.getElementById(\'status\').innerHTML =\n                    \'Thanks for logging in, \' + response.name + \'!\';\n                });\n              }\n        </script>\n    </head>\n    <body>\n        <div id="content"></div>\n        <script type="text/javascript" src="/static/script.js"></script>\n    </body>\n</html>')


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