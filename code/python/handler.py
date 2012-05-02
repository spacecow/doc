class TestHandler(webapp2.RequestHandler):
  def get(self):
    q = self.request.get("q") #get parameter q
    self.response.out.write(q)

app = webapp2.WSGIApplication([('/',MainPage),('/testform',TestHandler)],debug=True)
