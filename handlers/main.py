#!/usr/bin/env python
#
import webapp2
from webapp2_extras import jinja2

from model.client import Client
from model.line import Line
from model.invoice import Invoice
from webapp2_extras.users import users


class MainHandler(webapp2.RequestHandler):
    def get(self):
        usr = users.get_current_user()

        if usr:
            login_logout_url = users.create_logout_url("/")
        else:
            login_logout_url = users.create_login_url("/")

        invoices = Invoice.query().order(-Invoice.id)

        templates_val = {
            "invoices": invoices,
            "login_logout_url": login_logout_url,
            "usr": usr,
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("index.html", **templates_val))


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
