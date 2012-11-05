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


class MainPage(webapp2.RequestHandler):
	def get(self):
		
		templateValues = {
            'url': 'test variable',
		}
		path = os.path.join(os.path.dirname(__file__), 'base.html')
		self.response.out.write(template.render(path, templateValues))
#		self.response.out.write(template.render('base.html', {}))



class Guestbook(webapp2.RequestHandler):
    def post(self):
 		input = self.request.get('phrase')
		templateValues = {
            'wookie': translateToWookie(input),
		}
		path = os.path.join(os.path.dirname(__file__), 'base.html')
		self.response.out.write(template.render(path, templateValues))
		
 #     	self.response.out.write(cgi.escape(translateToWookie(self.request.get('phrase'))))
#       self.response.out.write(cgi.escape(self.request.get('phrase')))
#        self.response.out.write('</pre></body></html>')

app = webapp2.WSGIApplication([('/', MainPage),
                              ('/translate', Guestbook)],
                              debug=True)



def translateToWookie(englishWord):
	wookieLanguage = ['huurh ', 'uughghhhgh ','uuh ','raaaaaahhgh ','uughguughhhghghghhhgh ']
	random.shuffle(wookieLanguage)
	i = englishWord.__len__()/5 + 1
	translation = ""
	for num in range(0,i):
		translation += wookieLanguage[num]

	return translation




