#!/usr/bin/python
import os, sys
# Change working directory so relative paths (and template lookup) work again
os.chdir(os.path.dirname(__file__))

sys.path.append(os.path.dirname(__file__))

import bottle
import web_routes
# ... build or import your bottle application here ...
# Do NOT use bottle.run() with mod_wsgi
application = bottle.default_app()
