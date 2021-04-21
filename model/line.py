from google.appengine.ext import ndb


class Line(ndb.Model):
    concept = ndb.StringProperty(required=True)
    unit_price = ndb.FloatProperty(required=True)
    qty = ndb.IntegerProperty(required=True)
    gross_amount = ndb.FloatProperty()
    total_amount = ndb.FloatProperty()
