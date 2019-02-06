from tornado.web import url
from .handler import SmsHandler, RegisterHandler, LoginHandler

urlpattern = (
    ('/code/', SmsHandler),
    ('/register/', RegisterHandler),
    ('/login/', LoginHandler),
)
