import pytest
from bot import Crawler
@pytest.fixture(scope='session')
def crawler():
    return Crawler()
