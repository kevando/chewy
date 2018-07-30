
from google.appengine.ext import db


class Translation(db.Model):
    english = db.StringProperty(multiline=True)
    wookie = db.StringProperty(multiline=True)
    url_key = db.IntegerProperty()
    touched = db.IntegerProperty()
    date = db.DateTimeProperty(auto_now_add=True)
    ip_address = db.StringProperty(multiline=False)
    public = db.BooleanProperty(default=False)
