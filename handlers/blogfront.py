from google.appengine.ext import db
from handlers.blog import BlogHandler

# handler for main Blog Url
class BlogFrontHandler(BlogHandler):

    #
    def get(self):
        # variable to look up all posts by creation time and display latest 10
        posts = db.GqlQuery("select * from Post order by created desc limit 10")
        # render those posts to this html file
        self.render('front.html', posts=posts)