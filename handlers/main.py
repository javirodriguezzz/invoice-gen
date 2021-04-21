#!/usr/bin/env python
#
import webapp2
from webapp2_extras import jinja2

from model.client import Client
from model.line import Line
from model.invoice import Invoice


class MainHandler(webapp2.RequestHandler):
    def get(self):
        invoices = Invoice.query().order(-Invoice.id)

        templates_val = {
            "invoices": invoices,
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("index.html", **templates_val))


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
