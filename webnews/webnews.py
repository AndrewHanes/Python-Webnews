import json
import enum
from urllib.parse import urlencode
from urllib.request import urlopen
from urllib import request

API_KEY = open("private/apikey").read()
WEBNEWS_BASE = "https://webnews.csh.rit.edu/"
API_AGENT = "webnews-python"

class Actions(enum.Enum):
    user = "user"
    unread_counts = "unread_counts"
    newsgroups = "newsgroups"
    search = "search"
    compose = "compose"

def POST(action, api_key, args={}):
    if type(action) == Actions:
        action = action.value
    args['api_key'] = api_key
    args['api_agent'] = API_AGENT
    args = urlencode(args).encode('utf-8')
    req = request.Request(WEBNEWS_BASE + action)
    req.add_header('Accept', 'application/json')
    resp = urlopen(req, args).read().decode('utf-8')
    return json.loads(resp)


def GET(action, api_key, args={}):
    if type(action) == Actions:
        action = action.value
    args['api_key'] = api_key
    args['api_agent'] = API_AGENT
    args = urlencode(args)
    req = request.Request(WEBNEWS_BASE + action + '?' + args)
    req.add_header('Accept', 'application/json')
    resp = urlopen(req).read().decode('utf-8')
    #req = urlopen(WEBNEWS_BASE + action + '?' + args).readall()
    #req = req.decode('utf-8')
    return json.loads(resp)

def user(api_key = API_KEY):
    return GET(Actions.user, api_key=api_key)

def unread_counts(api_key = API_KEY):
    return GET(Actions.unread_counts, api_key=api_key)

def newsgroups(api_key = API_KEY):
    return GET(Actions.newsgroups, api_key=api_key)

def newsgroups_search(newsgroup, api_key=API_KEY):
    return GET("newsgroups/" + newsgroup, api_key=api_key)

def search(params = {}, api_key=API_KEY):
    return GET(Actions.search, api_key, params)

def post_specifics(newsgroup, index, params={}, api_key=API_KEY):
    return GET(str(newsgroup)+"/"+str(index), api_key, params)

def compose(newsgroup, subject, body, params={}, api_key=API_KEY):
    params['subject'] = subject
    params['body'] = body
    params['newsgroup'] = newsgroup
    return POST(Actions.compose, api_key, params)
