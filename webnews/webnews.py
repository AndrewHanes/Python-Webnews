import json
import urllib
import enum
from urllib.parse import urlencode
from urllib.request import urlopen

class Actions(enum.Enum):
    user = "user"
    unread_counts = "unread_counts"
    newsgroups = "newsgroups"


API_KEY = open("private/apikey").read()
WEBNEWS_BASE = "https://webnews.csh.rit.edu/"
API_AGENT = "webnews-python"

def GET(action, args={}, api_key = API_KEY):
    action = action.value
    args['api_key'] = api_key
    args['api_agent'] = API_AGENT
    args = urlencode(args)
    req = urlopen(WEBNEWS_BASE + action + '?' + args).readall().decode('utf-8')
    return json.loads(req)

def user(api_key = API_KEY):
    return GET(Actions.user)

def unread_counts(api_key = API_KEY):
    return GET(Actions.unread_counts)

resp = user()
print(resp)
resp = unread_counts()
print(resp)
