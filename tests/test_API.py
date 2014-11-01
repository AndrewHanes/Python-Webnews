from unittest import TestCase
from webnews import api
import os

class TestAPI(TestCase):

    def testSingleton(self):
        a = api.API(open("private/apikey").read())
        b = api.API(open("private/apikey").read())
        self.assertTrue(a is b)

    def setUp(self):
        if os.environ.get('WEBNEWS_API') == None:
            self.api = api.API(open("private/apikey").read())
        else:
            self.api = api.API(os.environ['WEBNEWS_API'])

    def test_POST(self):
        #Tests handled by other methods
        pass

    def test_GET(self):
        #Tests handled by other methods
        pass

    def test_unread_counts(self):
        self.api.unread_counts()

    def test_newsgroups(self):
        self.api.newsgroups()

    def test_newsgroups_search(self):
        self.api.newsgroups_search('control.cancel')

    def test_search(self):
        self.api.search()

    def test_post_specifics(self):
        self.api.post_specifics("control.cancel", 3)
