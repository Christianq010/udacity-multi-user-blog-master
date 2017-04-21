import webapp2

from helpers import *
from models.user import User

# Steve's Standard Convenience Functions
class BlogHandler(webapp2.RequestHandler):

    # 'write' turns self.response to a convenient function
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    # Call out template
    def render_str(self, template, **params):
        params['user'] = self.user
        return render_str(template, **params)

    # Call write and render_str to print out the template
    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

    def login(self, user):
        self.set_secure_cookie('user_id', str(user.key().id()))

    def logout(self):
        self.response.headers.add_header(
            'Set-Cookie',
            'user_id=; Path=/')

    def set_secure_cookie(self, name, val):
        cookie_val = make_secure_val(val)
        self.response.headers.add_header(
            'Set-Cookie',
            '%s=%s; Path=/' % (name, cookie_val))

    def initialize(self, *a, **kw):
        webapp2.RequestHandler.initialize(self, *a, **kw)
        uid = self.read_secure_cookie('user_id')
        self.user = uid and User.by_id(int(uid))

    def read_secure_cookie(self, name):
        cookie_val = self.request.cookies.get(name)
        return cookie_val and check_secure_val(cookie_val)