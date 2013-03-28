__author__ = 'redfish(lvrenkun@gmail.com)'

import os

import web

filename = os.environ.get('PYTHONSTARTUP')

print filename


print os.path.curdir
db = web.database(dbn='mysql',db='family',user='root',pw='admin')
bills  = db.select('member')

print bills