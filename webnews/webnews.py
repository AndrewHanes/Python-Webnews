from webnews import api

class WebnewsObject(object):
    def __init__(self, api_val):
        if type(api) == api.API:
            self._api = api_val
        else:
            self._api = api.API(api_val)


