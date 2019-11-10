import webapp2
from app import config
from app.views import *

app = webapp2.WSGIApplication([
    # ('/translations/(.*)', ListAllTranslations),
    # ('/uughghhhgh/(.*)', SharePage),
    ('/translate',TranslateHandler),
	('/()', TranslatePageHandler),
    # ('/ss', SessionHandler),
    ('/.*', NotFoundPageHandler)],
    debug=False,
    # config=sessionConfig
)
