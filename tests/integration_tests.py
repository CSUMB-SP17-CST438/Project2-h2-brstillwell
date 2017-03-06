import unittest
import app
from flask import Flask
import urllib2
import flask_testing, requests
from flask_testing import TestCase

import tempfile
import os
import json

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, app.app.config['DATABASE'] = tempfile.mkstemp()
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()
        

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(app.app.config['DATABASE'])
        
    def login(self, username, password):
        return self.app.post('/', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)

    def logout(self):
        return self.app.get('/', follow_redirects=True)
        
    def test_login_logout(self):
        rv = self.login('admin', 'admin')
        assert b'Allowed' in rv.data
        rv = self.logout()
        assert b'Thanks for logging in' in rv.data


class FlaskTestCase(unittest.TestCase):
    # Our first unit test - We are using the unittest
    # library, calling the _add_numbers route from the app
    # passing a pair of numbers, and checking that the
    # returned value, contained on the JSON response, match
    # the sum of those parameters
    def test_sum(self):
        tester = app.app.test_client(self)
        response = tester.get('/_add_numbers?a=2&b=6', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        # Check that the result sent is 8: 2+6
        self.assertEqual(json.loads(response.data), {"result": 8})

'''
class MyTest(flask_testing.LiveServerTestCase):

    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        # Default port is 5000
        app.config['LIVESERVER_PORT'] = 8943
        # Default timeout is 5 seconds
        app.config['LIVESERVER_TIMEOUT'] = 10
        return app

    def test_server_is_up_and_running(self):
        print ("the url: ", self.get_server_url())
        response = urllib2.urlopen(self.get_server_url())
        self.assertEqual(response.code, 200)
     '''   

if __name__ == '__main__':
    unittest.main()