#!/usr/bin/env python
#
import webapp2
from webapp2_extras import jinja2

from model.invoice import Invoice
import time


class NewInvoiceHandler(webapp2.RequestHandler):
    def get(self):

        templates_val = {
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("new_invoice.html", **templates_val))

    def post(self):
        str_id = self.request.get("edId", "")

        try:
            id = int(str_id)
        except ValueError:
            id = -1

        if id < 0:
            return self.redirect("/")
        else:
            invoice = Invoice(id=id)
            invoice.put()
            time.sleep(1)
            return self.redirect("/")


app = webapp2.WSGIApplication([
    ('/invoices/new', NewInvoiceHandler)
], debug=True)
