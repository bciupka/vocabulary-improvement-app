import pytest
from django.core.exceptions import ValidationError


pytestmark = pytest.mark.django_db


class TestLanguageModel:
    def test_str_method(self, language_factory):
        obj = language_factory(language_eng='test_lang')
        assert str(obj) == 'test_lang language'


class TestWordModel:
    def test_str_method(self, word_factory):
        obj = word_factory(word='test')
        assert str(obj) == 'test'

    def test_clean_method(self, word_factory):
        obj = word_factory(word='TEST-WORD')
        assert obj.word == 'test-word'


class TestLinkModel:
    def test_str_method(self, link_factory, imp_user_factory, language_factory, word_factory):
        user = imp_user_factory(username='test_user')
        lang2 = language_factory(symbol='tst')
        word1 = word_factory(word='tword')
        word2 = word_factory(language=lang2)
        obj = link_factory(user=user, base=word1, translation=word2)
        assert str(obj) == 'test_user - tword tst'

    def test_clean_method(self, link_factory, word_factory, language_factory):
        lang = language_factory()
        word1 = word_factory(language=lang)
        word2 = word_factory(language=lang)
        with pytest.raises(ValidationError, match="Same language in both words"):
            link_factory(base=word1, translation=word2)
