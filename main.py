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
# import cgi
import webapp2
# import random
# import os
# from google.appengine.ext.webapp import template
# import datetime
# import urllib
# from google.appengine.ext import webapp
# from google.appengine.ext.webapp.util import run_wsgi_app
# from webapp2_extras import sessions
# import logging
# from google.appengine.api import urlfetch
# import urllib

# from models import *
from views import *
# from helpers import *

app = webapp2.WSGIApplication([('/translations/(.*)', ListAllTranslations),
							  ('/uughghhhgh/(.*)', SharePage),
							  ('/()', MainPage),
                              ('/ss', SessionHandler),
							  ('/.*', NotFoundPageHandler)],
                              debug=False,
                              config=sessionConfig
                              )

# ---------------------------------------------------------------------
