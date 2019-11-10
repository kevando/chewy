import config
import random
import os
from webapp2_extras import sessions
from google.appengine.api import urlfetch
import urllib
from dude import *
from models import *

# def getTotalTranslations(self):

# 	totalTranslations = self.session.get('total_translations')

# 	if(totalTranslations):
# 		dude('we have a total!')
# 	else:
# 		self.session['total_translations'] = 0

# 	return totalTranslations

# def incrementTotalTranslations(self):

# 	totalTranslations = self.session.get('total_translations')

# 	if(totalTranslations):

# 		totalTranslations += 1
# 		self.session['total_translations'] = totalTranslations
# 	else:
# 		totalTranslations = 1
#         self.session['total_translations'] = totalTranslations



# ------------------------------------------------------------------------------

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
		translation = 'Language Recognized as Wookie'



	newTranslation = Translation(english = englishWord, wookie = translation, ip_address = ip)
	newTranslation.put()
	newCorrectUrlKey = int(newTranslation.key().id())

	# incrementTotalTranslations(self)

	return newCorrectUrlKey
