import json
import urllib
import enum

class Actions(enum.Enum):
    user = "user"
    unread_counts = "unread_counts"
    newsgroups = "newsgroups"


API_KEY = open("private/apikey").read()
WEBNEWS_BASE = "https://webnews.csh.rit.edu/"
API_AGENT = "webnews-python"

def GET(action, args={}):
    action = action.value
    args['api_key'] = API_KEY
    args['api_agent'] = API_AGENT
    args = urllib.parse.urlencode(args)
    req = urllib.request.urlopen(WEBNEWS_BASE + action + '?' + args).readall().decode('utf-8')
    return json.loads(req)

resp = GET(Actions.user)
print(resp)
