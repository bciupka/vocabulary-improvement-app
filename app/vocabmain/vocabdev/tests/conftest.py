from pytest_factoryboy import register
from vocabdev.tests.factories import ImpUserFactory, LanguageFactory, WordFactory, LinkFactory


register(ImpUserFactory)
register(LanguageFactory)
register(WordFactory)
register(LinkFactory)
