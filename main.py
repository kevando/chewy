#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import config
import cgi
import webapp2
import random
import os
from google.appengine.ext.webapp import template
import datetime
import urllib
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from webapp2_extras import sessions
import logging
from google.appengine.api import urlfetch
import urllib



# Define Model
class Translation(db.Model):
    english = db.StringProperty(multiline=True)
    wookie = db.StringProperty(multiline=True)
    url_key = db.IntegerProperty()
    touched = db.IntegerProperty()
    date = db.DateTimeProperty(auto_now_add=True)
    ip_address = db.StringProperty(multiline=False)
    public = db.BooleanProperty(default=False)

# ---------------------------------------------------------------------


class BaseHandler(webapp2.RequestHandler):

    # It works!

    def dispatch(self):
        # logging.info('infooooooooooo!')

        # Get a session store for this request.
        self.session_store = sessions.get_store(request=self.request)

        try:
            # Dispatch the request.
            webapp2.RequestHandler.dispatch(self)
        finally:
            # Save all sessions.
            self.session_store.save_sessions(self.response)

    @webapp2.cached_property
    def session(self):
        # Returns a session using the default cookie key.
        return self.session_store.get_session()

# ---------------------------------------------------------------------

# Landing function
class MainPage(BaseHandler):


	def get(self,urlKey):



		templateValues = {'placeholder':'Enter Human Language', 'key':config.getKey(), 'BASE_URL':config.getRootURL()}
		path = os.path.join(os.path.dirname(__file__), 'main.html')
		self.response.out.write(template.render(path, templateValues))

	def post(self,urlKey):
		userInput = self.request.get('phrase')
		newUrlKey = translateToWookie(userInput,self.request.remote_addr,self)
		translation = Translation.get_by_id(newUrlKey)


		templateValues = {
            'totalTranslations': getTotalTranslations(self),
            'placeholder':translation.english,
            'translation':translation.wookie,
            'translationId':translation.key().id(),
            'key':config.getKey(),
            'BASE_URL':config.getRootURL()
        }

		pushTranslationToZapier(templateValues)
		path = os.path.join(os.path.dirname(__file__), 'translated.html')
		self.response.out.write(template.render(path, templateValues))

# ---------------------------------------------------------------------

# Share function
class SharePage(BaseHandler):

	def get(self,urlKey):
		try:
		    urlKey
		except NameError:
		    urlKey = ''

		if(urlKey==''):
			self.redirect('/')
		if(urlKey!=''):
			tid = int(urlKey)
			translation = Translation.get_by_id(tid)
			if translation != None:
				templateValues = {'placeholder':translation.wookie,'translation':translation.english,'key':config.getKey(),'BASE_URL':config.getRootURL()}
			else:
				templateValues = {'placeholder':'uhhhughh arrahhrrhhhh','translation':'This isn\'t the page you\'re looking for...','key':config.getKey(),'BASE_URL':config.getRootURL()}
		path = os.path.join(os.path.dirname(__file__), 'share.html')
		self.response.out.write(template.render(path, templateValues))

# ---------------------------------------------------------------------

class ListAllTranslations(BaseHandler):
	def get(self,order):
		self.response.out.write("<style>td{border:solid 1px #B9B9B9;background:#E0E0E0;font-family:courier;font-size:12px;padding:2px;}</style>")
		self.response.out.write("<table><tr><td width='30'>ID</td><td width='200'>ENGLISH</td><td width='650'>WOOKIE</td><td width='200'>Date</td><td>IP</td></tr></strong>")
		translations = Translation.all()
#		translations.order("english")
		translations.order(order)
		translationSet = translations.fetch(limit=10000)
		for translated in translationSet:
			self.response.out.write('<tr>')
			self.response.out.write('<td>'+str(translated.key().id())+'</td>')
			self.response.out.write('<td>'+translated.english+'</td>')
			self.response.out.write('<td>'+translated.wookie+'</td>')
			self.response.out.write('<td>'+str(translated.date)+'</td>')
			self.response.out.write('<td>'+str(translated.ip_address)+'</td>')
			self.response.out.write('</tr>')
		#	translated.delete()
		self.response.out.write('</table>')

# ---------------------------------------------------------------------

class NotFoundPageHandler(BaseHandler):
	def get(self):
		self.error(404)
		templateValues = {'BASE_URL':config.getRootURL()}
		path = os.path.join(os.path.dirname(__file__), '404.html')
		self.response.out.write(template.render(path, templateValues))
# ---------------------------------------------------------------------


sessionConfig = {}
sessionConfig['webapp2_extras.sessions'] = {
    'secret_key': 'my-super-secret-key',
}
# ---------------------------------------------------------------------

app = webapp2.WSGIApplication([('/translations/(.*)', ListAllTranslations),
							  ('/uughghhhgh/(.*)', SharePage),
							  ('/()', MainPage),
							  ('/.*', NotFoundPageHandler)],
                              debug=False,
                              config=sessionConfig
                              )

# ---------------------------------------------------------------------


def getTotalTranslations(self):

	totalTranslations = self.session.get('total_translations')

	# logging.info('getTotalTranslations')
	# logging.info(totalTranslations)

	if(totalTranslations):
		logging.info('we have a total!')
	else:
		# logging.info('we dont have a total. need to init')
		self.session['total_translations'] = 0

	return totalTranslations

def incrementTotalTranslations(self):

	totalTranslations = self.session.get('total_translations')

	# logging.info('incrementTotalTranslations')
	# logging.info(totalTranslations)

	if(totalTranslations):
		# logging.info('we have a total! inc')
		totalTranslations += 1
		# logging.info('incrementTotalTranslations')
		# logging.info(totalTranslations)
		self.session['total_translations'] = totalTranslations
	else:
		# logging.info('we dont have a total. soome ting wrong')
		totalTranslations = 1
		# logging.info('incrementTotalTranslations')
		# logging.info(totalTranslations)
        self.session['total_translations'] = totalTranslations

def pushTranslationToZapier(templateValues):
    logging.info("WTF")
    try:
        payload = urllib.urlencode(templateValues)
        headers = {}
        result = urlfetch.fetch(
            url='https://hooks.zapier.com/hooks/catch/1835221/anx2ol/',
            payload=payload,
            method=urlfetch.POST,
            headers=headers)
        logging.info(result.content)
    except urlfetch.Error:
        logging.exception('Caught exception fetching url')


def translateToWookie(englishWord,ip,self):
	wookieLanguage = [	'huurh',
						'uughghhhgh',
						'uugggh',
						'raaaaaahhgh',
						'hnnnhrrhhh',
						'huuguughghg',
						'aarrragghuuhw',
						'aaahnruh',
						'huurh','uughghhhgh',
						'uggguh','raaaaaahhgh',
						'uughguughhhghghghhhgh',
						'huuguughghg','aarrragghuuhw',
						'aaaaahnr','huurh','uughghhhgh',
						'uuh','raaaaaahhgh','uughguughhhghghghhhgh',
						'huuguughghg','aarrragghuuhw',
						'aaaaahnr','huurh','uughghhhgh',
						'wuuh','raaaaaahhgh',
						'uughguughhhghghghhhgh',
						'huuguughghg','aarrragghuuhw',
						'awwgggghhh','huurh','wrrhwrwwhw',
						'wrrhw','raaaaaahhgh',
						'uughguughhhghghghhhgh',
						'huuguughghg','aguhwwgggghhh',
						'aaaaahnr']
	random.shuffle(wookieLanguage)
	i = englishWord.__len__()/6 + 1
	translation = ""
	for num in range(0,i):
		translation += wookieLanguage[num]+' '

	# now do some specific translations for frequent input
	if(englishWord == 'hi' or englishWord == 'hello'):
		translation = 'nuuawh'

	if(englishWord in wookieLanguage):
		translation = 'i am wookie, hear me roar!'

	if(englishWord == 'A simple tool that helps you talk with Chewy.' or englishWord == 'A simple tool that helps you talk with Chewy'):
		translation = 'aarrragghuuhw aarrragghuuhw raaaaaahhgh'


	if(englishWord.find('uughghhhgh') != -1 or
	englishWord.find('raaaaaahhgh') != -1 or
	englishWord.find('huuguughghg') != -1 or
	englishWord.find('uughguughhhghghghhhgh') != -1 or
	englishWord.find('aarrragghuuhw') != -1 or
	englishWord.find('uughguughhhghghghhhgh') != -1 or
	englishWord.find('wrrhwrwwhw') != -1 or
	englishWord.find('huuguughghg') != -1 or
	englishWord.find('hnnnhrrhhh') != -1 or
	englishWord.find('aarrragghuuhw') != -1 or
	englishWord.find('aarrragghuuhw') != -1 or
	englishWord.find('huuguughghg') != -1 or
	englishWord.find('uughghhhgh') != -1 or
	englishWord.find('aaahnruh') != -1 or
	englishWord.find('raaaaaahhgh') != -1 or
	englishWord.find('uughghhhgh') != -1 or
	englishWord.find('uughguughhhghghghhhgh') != -1 or
	englishWord.find('aguhwwgggghhh') != -1 or
	englishWord.find('huuguughghg') != -1 or
	englishWord.find('aarrragghuuhw') != -1 or
	englishWord.find('uughghhhgh') != -1 or
	englishWord.find('huuguughghg') != -1 or
	englishWord.find('raaaaaahhgh') != -1 or
	englishWord.find('awwgggghhh') != -1):
		translation = '** Invalid Input! Language Recognized as Wookie**'



	newTranslation = Translation(english = englishWord, wookie = translation, ip_address = ip)
	newTranslation.put()
	newCorrectUrlKey = int(newTranslation.key().id())

	incrementTotalTranslations(self)

	return newCorrectUrlKey
