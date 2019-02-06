import tornado
from tornado import web
import wtforms_json
from peewee_async import Manager

from MxForum.settings import settings, database
from MxForum.urls import urlpattern

if __name__ == '__main__':
    wtforms_json.init()
    app = web.Application(urlpattern, debug=True, **settings)
    app.listen(8888)
    objects = Manager(database)
    database.set_allow_sync(False)
    app.objects = objects
    io_loop = tornado.ioloop.IOLoop.current().start()
