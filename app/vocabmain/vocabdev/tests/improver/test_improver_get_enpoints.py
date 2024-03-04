import pytest


pytestmark = pytest.mark.django_db


class TestLanguageEndpoints:
    endpoint = '/api/language/'

    def test_get_all_enpoint(self, language_factory, api_client):
        language_factory.create_batch(8)
        response = api_client().get(self.endpoint)
        assert response.status_code == 200
        assert len(response.data) == 8

    def test_get_by_symbol_endpoint(self, language_factory, api_client):
        language_factory(symbol='tst')
        language_factory.create_batch(2)
        response = api_client().get(f'{self.endpoint}tst/')
        assert response.status_code == 200
        assert isinstance(response.data, dict)


class TestWordEndpoints:
    endpoint = '/api/word/'

    def test_get_all_endpoint(self, word_factory, api_client, imp_user_factory):
        user = imp_user_factory()
        word_factory.create_batch(8)
        client = api_client()
        client.force_authenticate(user=user)
        response = client.get(self.endpoint)
        assert response.status_code == 200
        assert len(response.data) == 8

    def test_get_by_lang_endpoint(self, word_factory, api_client, imp_user_factory, language_factory):
        user = imp_user_factory()
        lang = language_factory(symbol='tst')
        word_factory(word='bylang', language=lang)
        word_factory(word='bylangtwo', language=lang)
        word_factory.create_batch(2)
        client = api_client()
        client.force_authenticate(user=user)
        response = client.get(f'{self.endpoint}getlang/tst/bylang/')
        assert response.status_code == 200
        assert len(response.data) == 1


    def test_list_by_lang_endpoint(self, word_factory, api_client, imp_user_factory, language_factory):
        user = imp_user_factory()
        lang = language_factory(symbol='tst')
        word_factory(word='bylang', language=lang)
        word_factory(word='bylangtwo', language=lang)
        word_factory.create_batch(2)
        client = api_client()
        client.force_authenticate(user=user)
        response = client.get(f'{self.endpoint}listlang/tst/')
        assert response.status_code == 200
        assert len(response.data) == 2


class TestLinkEndpoints:
    endpoint = '/api/link/'

    def test_paginated_get_endpoint(self, link_factory, api_client, imp_user_factory, language_factory):
        user = imp_user_factory()
        client = api_client()
        client.force_authenticate(user=user)
        lang1 = language_factory(symbol='lat')
        lang2 = language_factory(symbol='law')
        link_factory.create_batch(
            6,
            user=user,
            base__language=lang1,
            translation__language=lang2
        )
        response = client.get(f'{self.endpoint}?amount=5&lang1=lat&lang2=law')
        response_2 = client.get(f'{self.endpoint}?amount=5&lang1=lat&lang2=law&page=3')
        assert response.status_code == 200
        assert len(response.data) == 4
        assert len(response.data['results']) == 3
        assert response.data['next'] is not None
        assert response.data['previous'] is None
        assert response.data['count'] == 5
        assert response_2.status_code == 404

    def test_random_list_endpoint(self, link_factory, language_factory, api_client, imp_user_factory):
        user = imp_user_factory()
        client = api_client()
        client.force_authenticate(user=user)
        lang1 = language_factory(symbol='lat')
        lang2 = language_factory(symbol='law')
        link_factory.create_batch(
            6,
            user=user,
            base__language=lang1,
            translation__language=lang2
        )
        response = client.get(f'{self.endpoint}random_list/?amount=5&lang1=lat&lang2=law')
        assert response.status_code == 200
        assert len(response.data) == 5
