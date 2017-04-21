from handlers.blog import BlogHandler
from models.post import Post
from helpers import *

class NewPostHandler(BlogHandler):

    # a get to render newpost to html
    def get(self):
        if self.user:
            self.render("newpost.html")
        else:
            error = "You must be signed in to create a post."
            self.render("base.html", access_error=error)

    # confirm new post by checking input fields & log in
    def post(self):
        if not self.user:
            return self.redirect('/login')

        subject = self.request.get('subject')
        content = self.request.get('content')

        if subject and content:
            p = Post(parent=blog_key(), subject=subject,
                     content=content, user_id=self.user.key().id())
            # put - stores post into the database
            p.put()
            # redirect to the post-id url fetched from datastore
            self.redirect('/%s' % str(p.key().id()))
        else:
            error = "Please fill up the fields."
            self.render("newpost.html", subject=subject,
                        content=content, error=error)