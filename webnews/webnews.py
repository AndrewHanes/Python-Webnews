import json
import enum
from urllib.parse import urlencode
from urllib.request import urlopen

API_KEY = open("private/apikey").read()
WEBNEWS_BASE = "https://webnews.csh.rit.edu/"
API_AGENT = "webnews-python"

class Actions(enum.Enum):
    user = "user"
    unread_counts = "unread_counts"
    newsgroups = "newsgroups"
    search = "search"

def GET(action, api_key, args={}):
    if type(action) == Actions:
        action = action.value
    args['api_key'] = api_key
    args['api_agent'] = API_AGENT
    args = urlencode(args)
    req = urlopen(WEBNEWS_BASE + action + '?' + args).readall().decode('utf-8')
    return json.loads(req)

def user(api_key = API_KEY):
    return GET(Actions.user, api_key=api_key)

def unread_counts(api_key = API_KEY):
    return GET(Actions.unread_counts, api_key=api_key)

def newsgroups(api_key = API_KEY):
    return GET(Actions.newsgroups, api_key=api_key)

def newsgroups_search(newsgroup, api_key=API_KEY):
    return GET("newsgroups/" + newsgroup, api_key=api_key)

def search(params = {}, api_key=API_KEY):
    return GET(Actions.search, params, api_key)