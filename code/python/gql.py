posts = db.GqlQuery("select * from Post order by created desc")
posts = Post.all().order('-created') #same
posts = list(posts) #detach from query
