from gevent.wsgi import WSGIServer
from gevent import monkey; monkey.patch_all()
from pure_flask import app

http_server = WSGIServer(('', 5001), app)
http_server.serve_forever()