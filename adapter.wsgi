#!/usr/bin/python
import bottle, os, sys
# Change working directory so relative paths (and template lookup) work again
os.chdir(os.path.dirname(__file__))

sys.path.append(os.path.dirname(__file__))

# ... build or import your bottle application here ...
# Do NOT use bottle.run() with mod_wsgi

import web_routes

application = bottle.default_app()
