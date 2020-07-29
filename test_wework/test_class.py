class TestDemo:
    _a = None

    def test_a(self):
        self._a = "ABC"
        print(TestDemo._a)
        print(self._a)

