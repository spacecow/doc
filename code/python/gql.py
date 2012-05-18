posts = db.GqlQuery("select * from Post order by created desc")
posts = Post.all().order('-created') #same
