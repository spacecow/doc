  ...
  self.redirect('/thanks')

class ThanksHandler(webapp2.RequestHandler):
  def get(self):
    self.response.out.write("Thanks! That's totally valid!")
app = webapp2.WSGIApplication([('/',MainPage),('/thanks',ThanksHandler)],debug=True)

