import os
#-----------------------------------------------------------------
#Segment Keys

LOCAL_KEY = "V8k774grRkJCZvyKkAxIcaqaO0tnQUmy"
LIVE_KEY = "testkey"

def getKey():
	if os.environ['SERVER_SOFTWARE'].startswith('Development'):
		return LOCAL_KEY
	else:
		return LIVE_KEY

#-----------------------------------------------------------------
#BaseURL

BASE_URL = "/"

def getRootURL():
	return BASE_URL