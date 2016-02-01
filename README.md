# How to set up local instance of WookieTranslator.com

1. Go to: https://cloud.google.com/appengine/downloads#Google_App_Engine_SDK_for_Python and then download Google App Engine SDK for your platform

2. Use the github link in terminal: ```git clone https://github.com/kevando/chewy.git```

3. Use the git command checkout to get the latest branch version. ```git checkout "branch name"```

4. Now you have the up-to-date repo and so navigate to the folder containing the webapp and then run in terminal: ```dev_appserver.py chewy/```

5. Go to ```localhost:8080``` in your browser and your local instance of the website should be working. Now it can be used for testing changes locally before committing them to github.
