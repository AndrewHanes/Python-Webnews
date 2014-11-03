from webnews import api
import json

class WebnewsObject(object):
    def __init__(self, api_val):
        if type(api) == api.API:
            self._api = api_val
        else:
            self._api = api.API(api_val)

    def populate(self, ng):
        for k in ng:
            setattr(self, k, ng[k])

class Newsgroup(WebnewsObject):

    #For autocomplete in IDE mostly.  Not needed to compile
    unread_class, status, updated_at, created_at, name, newest_date, unread_count = ([None for i in range(7)])

    def __init__(self, api_val, name):
        super(Newsgroup, self).__init__(api_val)
        ng = self._api.newsgroups_search(name)
        self.populate(ng['newsgroup'])
        print([i for i in ng['newsgroup'].keys()])
