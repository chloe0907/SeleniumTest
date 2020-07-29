from test_wework.index import Index

class TestContacts:

    def setup(self):
        self.index = Index()

    def test_add_contact(self):
        result = self.index.goto_add_contact().add_contact()
        assert result == True
