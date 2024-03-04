import pytest
from pytest_factoryboy import register
from vocabdev.tests.factories import ImpUserFactory, LanguageFactory, WordFactory, LinkFactory
from rest_framework.test import APIClient


register(ImpUserFactory)
register(LanguageFactory)
register(WordFactory)
register(LinkFactory)

@pytest.fixture
def api_client():
    return APIClient
