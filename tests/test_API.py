from unittest import TestCase
from webnews import api

class TestAPI(TestCase):
    def test_POST(self):
        self.api = api.API(open("private/apikey").read())

    def test_GET(self):
        self.fail()

    def test_unread_counts(self):
        self.fail()

    def test_newsgroups(self):
        self.fail()

    def test_newsgroups_search(self):
        self.fail()

    def test_search(self):
        self.fail()

    def test_post_specifics(self):
        self.fail()