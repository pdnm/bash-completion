import pytest


class TestA2x:
    @pytest.mark.complete("a2x ")
    def test_1(self, completion):
        assert completion
