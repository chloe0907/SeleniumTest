# from pomodule.base import Base
from pomodule.index import Index


class TestRegister:

    def setup(self):
        self.index = Index()

    def test_register(self):

        result = self.index.goto_register().register()
        assert result == True