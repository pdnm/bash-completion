import pytest


class TestPylint3(object):

    @pytest.mark.complete("pylint-3 --v")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("pylint-3 http.clien")
    def test_2(self, completion):
        assert completion.list