import tornado.ioloop
import tornado.web
import os, time

from config import *

import base64
import uuid

cookie_secret = base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes)



class HomeHandler(tornado.web.RequestHandler):
	def get(self):
		if COOKIE:
			if self.get_secure_cookie("username"):
				return self.render("templates"+ NAME_HOME +".html")
			else:
				self.redirect(NAME_ROOT)
		else:
			return self.render("templates"+ NAME_HOME +".html")

class RootHandler(tornado.web.RequestHandler):
	def get(self):
		return self.render("templates/root.html")


class LoginHandler(tornado.web.RequestHandler):
	def get(self):
		if COOKIE:
			if not self.get_secure_cookie("username"):
				return self.render("templates"+ NAME_LOGIN +".html", error=None)
			else:
				self.redirect(NAME_HOME)
		else:
			return self.render("templates"+ NAME_LOGIN +".html", error=None)
		
	def post(self):
		username = self.get_argument("username")
		password = self.get_argument("password")
		if username == USERNAME and password == PASSWORD:
			if COOKIE:
				self.set_secure_cookie("username", username)
			self.redirect(NAME_HOME)
		else:
			self.render("templates"+ NAME_LOGIN +".html", error="Login failed")


class ServerHeaderTransform(tornado.web.OutputTransform):
    def transform_first_chunk(self, status_code, headers, chunk, finishing):
        headers['Server'] = HEADER_NAME
        return status_code, headers, chunk


paths = [
	(r'/(favicon\.ico)', tornado.web.StaticFileHandler, {'path': 'static/'}),
	(r'/static/(.*)', tornado.web.StaticFileHandler, {'path': 'static/'}),
]

if HOME:
	paths.append((NAME_HOME, HomeHandler))
if LOGIN:
	paths.append((NAME_LOGIN, LoginHandler))
if ROOT:
	paths.append((NAME_ROOT, RootHandler))

if COOKIE:
	application = tornado.web.Application(paths, transforms=[ServerHeaderTransform], cookie_secret=cookie_secret)
else:	
	application = tornado.web.Application(paths, transforms=[ServerHeaderTransform])

if __name__ == "__main__":
	application.listen(PORT)
	tornado.ioloop.IOLoop.instance().start()

