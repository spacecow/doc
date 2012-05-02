form="""
  <form method="post">
  <label>Free Field <input name="q" value="%(q)s"></label> 
  <div style="color: red">%(error)s</div>
  </form>
"""
def validation_function(q):
  reutrn ...

class MainPage(webapp2.RequestHandler):
  def write_form(self,error="",q=""):
    self.response.out.write(form % {'error':error,'q':q})

  def get(self):
    self.write_form()

  def post(self):
    user_q = self.request.get('q')
    q      = validation_function(user_q)
  
    if not q:
      self.write_form("Invalid form.",user_q)
    else:
      self.response.out.write("Thanks! That's totally valid!")

