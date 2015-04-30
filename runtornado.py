from sys import argv

from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from server import app

import properties

SETTINGS = {}
properties.load_server_settings(SETTINGS)

http_server = HTTPServer(WSGIContainer(app))
if len(argv)==2:
    http_server.listen(int(argv[1]))
else:
    http_server.listen(int(SETTINGS['PORT']))
IOLoop.instance().start()

# the following didn't help much
# http_server = HTTPServer(WSGIContainer(app))
# http_server.bind(int(SETTINGS['PORT']))
# http_server.start(4)
# IOLoop.instance().start()
