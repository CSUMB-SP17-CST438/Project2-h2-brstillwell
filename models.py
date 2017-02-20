# models.py
import flask_sqlalchemy, app, os

#app.app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:admin@localhost/postgres'
app.app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')

db = flask_sqlalchemy.SQLAlchemy(app.app)
class ChatRoom(db.Model):
    id = db.Column(db.Integer, primary_key=True) # key
    user = db.Column(db.String(120))
    image = db.Column(db.String(200))
    message = db.Column(db.String(140))
    
    
    def __init__(self, u, i, m):
        self.user = u
        self.image = i
        self.message = m
    
    def __repr__(self): # what's __repr__?
        return '%s' % self.user + '|><|%s' % self.image + '|><|%s' % self.message
        
class Users(db.Model):
    user = db.Column(db.String(120), primary_key=True)
    image = db.Column(db.String(200), primary_key=True)
    
    def __init__(self, u, i):
        self.user = u
        self.image = i
    
    def __repr__(self): # what's __repr__?
        return '%s' % self.user + '|><|%s' % self.image