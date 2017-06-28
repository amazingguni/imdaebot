import pytest
from bot import create_bot
from bot import Bot

class TestBot:
    def test_create(self):
        assert isinstance(create_bot(), Bot)
        