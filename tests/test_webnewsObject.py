from unittest import TestCase
from webnews import webnews
from webnews import api

class TestWebnewsObject(TestCase):
    def test___init__(self):
        t = webnews.WebnewsObject('asdfasdf')
        self.assertTrue(type(t._api) == api.APINonSingle)
        apiobj = t._api
        a = webnews.WebnewsObject(apiobj)
        self.assertTrue(type(a._api) == api.APINonSingle)
