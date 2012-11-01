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

from google.appengine.api import users

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("""
          <html>
            <body>
			  <h1>Enter something you would like to have translated to Wookie</h1>
              <form action="/sign" method="post">
                <div><input name="phrase" /></div>
                <div><input type="submit" value="Sign Guestbook"></div>
              </form>
            </body>
          </html>""")


class Guestbook(webapp2.RequestHandler):
    def post(self):
        self.response.out.write('<html><body>Your Wookie Said:<pre>')
        self.response.out.write('uuughhhguhh hhguhuhuhgg')
#        self.response.out.write(cgi.escape(self.request.get('content')))
#       self.response.out.write(cgi.escape(self.request.get('phrase')))
        self.response.out.write('</pre></body></html>')

app = webapp2.WSGIApplication([('/', MainPage),
                              ('/sign', Guestbook)],
                              debug=True)