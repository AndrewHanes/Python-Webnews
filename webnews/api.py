import json
import enum
from urllib.parse import urlencode
from urllib.request import urlopen
from urllib import request


class API:
    def __init__(self, api_key, agent = "webnews-python", webnews_base = "https://webnews.csh.rit.edu/"):
        self.agent = agent
        self.api_key = api_key
        self.webnews_base = webnews_base

    class Actions(enum.Enum):
        user = "user"
        unread_counts = "unread_counts"
        newsgroups = "newsgroups"
        search = "search"
        compose = "compose"

    def POST(self, action, args={}):
        if type(action) == API.Actions:
            action = action.value
        args['api_key'] = self.api_key
        args['api_agent'] = self.agent
        args = urlencode(args).encode('utf-8')
        req = request.Request(self.webnews_base+ action)
        req.add_header('Accept', 'application/json')
        resp = urlopen(req, args).read().decode('utf-8')
        return json.loads(resp)


    def GET(self, action, args={}):
        if type(action) == API.Actions:
            action = action.value
        args['api_key'] = self.api_key
        args['api_agent'] = self.agent
        args = urlencode(args)
        req = request.Request(self.webnews_base + action + '?' + args)
        req.add_header('Accept', 'application/json')
        resp = urlopen(req).read().decode('utf-8')
        #req = urlopen(WEBNEWS_BASE + action + '?' + args).readall()
        #req = req.decode('utf-8')
        return json.loads(resp)

    def user(self):
        return self.GET(API.Actions.user)

    def unread_counts(self):
        return self.GET(API.Actions.unread_counts)

    def newsgroups(self):
        return self.GET(API.Actions.newsgroups)

    def newsgroups_search(self, newsgroup):
        return self.GET("newsgroups/" + newsgroup)

    def search(self, params = {}):
        return self.GET(API.Actions.search, params)

    def post_specifics(self, newsgroup, index, params={}):
        return self.GET(str(newsgroup)+"/"+str(index), params)

    def compose(self, newsgroup, subject, body, params={}):
        params['subject'] = subject
        params['body'] = body
        params['newsgroup'] = newsgroup
        return self.POST(API.Actions.compose, params)