from google.appengine.ext import ndb

from client import Client
from line import Line


class Invoice(ndb.Model):
    hora = ndb.DateTimeProperty(auto_now_add=True)
    id = ndb.IntegerProperty(indexed=True, required=True)
    emisor = ndb.KeyProperty(kind=Client)
    receiver = ndb.KeyProperty(kind=Client)
    invoice_line = ndb.KeyProperty(kind=Line)
    autor = ndb.StringProperty()
