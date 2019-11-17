import webapp2
import os
from google.appengine.ext.webapp import template
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from webapp2_extras import sessions
import json
import config
from models import *
from helpers import *


# class BaseHandler(webapp2.RequestHandler):


#     # It works!

#     def dispatch(self):

#         # Get a session store for this request.
#         self.session_store = sessions.get_store(request=self.request)

#         try:
#             # Dispatch the request.
#             webapp2.RequestHandler.dispatch(self)
#         finally:
#             # Save all sessions.
#             self.session_store.save_sessions(self.response)

#     @webapp2.cached_property
#     def session(self):
#         # Returns a session using the default cookie key.
#         return self.session_store.get_session()

# ---------------------------------------------------------------------


class TranslatePageHandler(webapp2.RequestHandler):

    def get(self, urlKey):

        templateValues = {
            'placeholder': 'Enter Human Language',
            'key': config.getKey(),
            'BASE_URL': config.getRootURL(),
            # 'totalTranslations': getTotalTranslations(self),
        }
        path = os.path.join(os.path.dirname(__file__), 'html/main.html')
        self.response.out.write(template.render(path, templateValues))


class TranslateHandler(webapp2.RequestHandler):
    def post(self):

        # Grab user input
        data = json.loads(self.request.body)
        english = data['english']

        # Translate to wookie. Not ideal code...
        newUrlKey = translateToWookie(english, self.request.remote_addr, self)
        translation = Translation.get_by_id(newUrlKey)

        self.response.out.write(translation.wookie)

# --------------------------------------------------------------
# Set Session Data
# --------------------------------------------------------------

# class SessionHandler(BaseHandler):

#     def post(self):

#         # Get new variables from ajax request

#         sessionData = json.loads(self.request.body)

#         # Might error if session var doesnt already exist
#         for sessionVariable in sessionData:
#             self.session[sessionVariable] = sessionData[sessionVariable]

#         # Tell client a nice story

#         self.response.out.write('All Good')


# ---------------------------------------------------------------------

# Share function
# class SharePage(BaseHandler):

# 	def get(self,urlKey):
# 		try:
# 		    urlKey
# 		except NameError:
# 		    urlKey = ''

# 		if(urlKey==''):
# 			self.redirect('/')
# 		if(urlKey!=''):
# 			tid = int(urlKey)
# 			translation = Translation.get_by_id(tid)
# 			if translation != None:
# 				templateValues = {'placeholder':translation.wookie,'translation':translation.english,'key':config.getKey(),'BASE_URL':config.getRootURL()}
# 			else:
# 				templateValues = {'placeholder':'uhhhughh arrahhrrhhhh','translation':'This isn\'t the page you\'re looking for...','key':config.getKey(),'BASE_URL':config.getRootURL()}
# 		path = os.path.join(os.path.dirname(__file__), 'share.html')
# 		self.response.out.write(template.render(path, templateValues))

# ---------------------------------------------------------------------

# class ListAllTranslations(BaseHandler):
# 	def get(self,order):
# 		self.response.out.write("<style>td{border:solid 1px #B9B9B9;background:#E0E0E0;font-family:courier;font-size:12px;padding:2px;}</style>")
# 		self.response.out.write("<table><tr><td width='30'>ID</td><td width='200'>ENGLISH</td><td width='650'>WOOKIE</td><td width='200'>Date</td><td>IP</td></tr></strong>")
# 		translations = Translation.all()
# #		translations.order("english")
# 		translations.order(order)
# 		translationSet = translations.fetch(limit=10000)
# 		for translated in translationSet:
# 			self.response.out.write('<tr>')
# 			self.response.out.write('<td>'+str(translated.key().id())+'</td>')
# 			self.response.out.write('<td>'+translated.english+'</td>')
# 			self.response.out.write('<td>'+translated.wookie+'</td>')
# 			self.response.out.write('<td>'+str(translated.date)+'</td>')
# 			self.response.out.write('<td>'+str(translated.ip_address)+'</td>')
# 			self.response.out.write('</tr>')
# 		#	translated.delete()
# 		self.response.out.write('</table>')

# ---------------------------------------------------------------------

class NotFoundPageHandler(webapp2.RequestHandler):
    def get(self):
        self.error(404)
        templateValues = {'BASE_URL': config.getRootURL()}
        path = os.path.join(os.path.dirname(__file__), 'html/404.html')
        self.response.out.write(template.render(path, templateValues))
# ---------------------------------------------------------------------


# sessionConfig = {}
# sessionConfig['webapp2_extras.sessions'] = {
#     'secret_key': 'my-super-secret-key',
# }
# ---------------------------------------------------------------------
