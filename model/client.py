from google.appengine.ext import ndb


class Client(ndb.Model):
    cif = ndb.StringProperty(required=True, indexed=True)
    name = ndb.StringProperty(required=True, indexed=True)
    address = ndb.StringProperty(required=True)
    city = ndb.StringProperty(required=True)
    provincia = ndb.StringProperty(required=True)
    address_code = ndb.IntegerProperty(required=True)
    country = ndb.StringProperty(required=True)
    contact_user = ndb.StringProperty(required=True)
    email = ndb.StringProperty()
    phone = ndb.StringProperty()