from unittest import TestCase
from webnews import api

class TestAPI(TestCase):

    def setUp(self):
        self.api = api.API(open("private/apikey").read())

    def test_POST(self):
        pass

    def test_GET(self):
        pass

    def test_unread_counts(self):
        print(self.api.unread_counts())

    def test_newsgroups(self):
        print(self.api.newsgroups())

    def test_newsgroups_search(self):
        print(self.api.newsgroups_search('control.cancel'))

    def test_search(self):
        print(self.api.search())

    def test_post_specifics(self):
        print(self.api.post_specifics("csh.test", 2))
