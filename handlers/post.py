from google.appengine.ext import db
from handlers.blog import BlogHandler
from helpers import *

# Look up a post on the google datastore
class PostHandler(BlogHandler):

    def get(self, post_id):
        # retrieve post from its id and return 404 if id doesn't exist
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)

        comments = db.GqlQuery(
            "select * from Comment where ancestor is :1 order by created desc limit 10", key)

        if not post:
            self.error(404)
            return

        self.render("permalink.html", post=post, comments=comments)