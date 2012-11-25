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
import cgi
import webapp2
import random
import os
from google.appengine.ext.webapp import template
from google.appengine.api import users
import datetime
import urllib
from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.api import mail


# Define Model
class Translation(db.Model):
    english = db.StringProperty(multiline=True)
    wookie = db.StringProperty(multiline=True)
    url_key = db.IntegerProperty()
    touched = db.IntegerProperty()
    date = db.DateTimeProperty(auto_now_add=True)

# Landing function
class MainPage(webapp2.RequestHandler):
	def get(self,urlKey):
		
		if(urlKey==''):
			templateValues = {'wookie': '...'}
		else:
			tid = int(urlKey)
			translation = Translation.get_by_id(tid)
			templateValues = {'wookie': translation.wookie}
			

		path = os.path.join(os.path.dirname(__file__), 'base.html')
		self.response.out.write(template.render(path, templateValues))
		
	def post(self,urlKey):
		userInput = self.request.get('phrase')
		allTranslations = Translation.all()
		allTranslations.filter('english =',userInput)
		
		
		if(allTranslations.count() == 1):
			result = allTranslations.get()
			newUrlKey = str(result.key().id())
		if(allTranslations.count() < 1):
			newUrlKey =  translateToWookie(userInput)
		if(allTranslations.count() > 1):
			newUrlKey = "66666"
			
		self.redirect("/"+newUrlKey)
		
class Email(webapp2.RequestHandler):
    def post(self):
		kev ="asdf"
		message = mail.EmailMessage(sender="khabich@gmail.com",
		                            subject=self.request.get('subject'))

		message.to = "kevin.h@roybiv.net"
		message.body = ' '+self.request.get('body')

		message.send()
		self.redirect("/")

		
class ListAllTranslations(webapp2.RequestHandler):
	def get(self):
		self.response.out.write("<style>td{border:solid 1px #B9B9B9;background:#E0E0E0;}</style>")
		self.response.out.write("<table><tr><td width='30'>ID</td><td>ENGLISH</td><td>WOOKIE</td><td>Date</td></tr>")
		translations = Translation.all()
#		translations.order("english")
		translationSet = translations.fetch(limit=100)
		for translated in translationSet:
			self.response.out.write('<tr>')
			self.response.out.write('<td>'+str(translated.key().id())+'</td>')
			self.response.out.write('<td>'+translated.english+'</td>')
			self.response.out.write('<td>'+translated.wookie+'</td>')
			self.response.out.write('<td>'+str(translated.date)+'</td>')
			self.response.out.write('</tr>')
		#	translated.delete()	
		self.response.out.write('</table>')
		
		

app = webapp2.WSGIApplication([('/translations', ListAllTranslations),
							  ('/email', Email),
							  ('/(.*)', MainPage)],
                              debug=True)



def translateToWookie(englishWord):
	wookieLanguage = ['huurh ', 'uughghhhgh ','uuh ','raaaaaahhgh ','uughguughhhghghghhhgh ', 'huuguughghg ','aarrragghuuhw ','aaaaahnr ','huurh ', 'uughghhhgh ','uuh ','raaaaaahhgh ','uughguughhhghghghhhgh ', 'huuguughghg ','aarrragghuuhw ','aaaaahnr ','huurh ', 'uughghhhgh ','uuh ','raaaaaahhgh ','uughguughhhghghghhhgh ', 'huuguughghg ','aarrragghuuhw ','aaaaahnr ','huurh ', 'uughghhhgh ','uuh ','raaaaaahhgh ','uughguughhhghghghhhgh ', 'huuguughghg ','aarrragghuuhw ','aaaaahnr ']
	random.shuffle(wookieLanguage)
	i = englishWord.__len__()/5 + 1
	translation = ""
	for num in range(0,i):
		translation += wookieLanguage[num]

	newTranslation = Translation(english = englishWord, wookie = translation).put()

	# need better way to get this data
	allTranslations = Translation.all()
	allTranslations.filter('english =',englishWord)
	result = allTranslations.get()
	newUrlKey = str(result.key().id())
	
	return newUrlKey




