import factory
from vocabdev.account.models import ImpUser
from vocabdev.improver.models import Language, Word, Link


class ImpUserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = ImpUser

    username = factory.Sequence(lambda x: f'user_{x}')
    email = factory.LazyAttribute(lambda x: f"{x.username}@smth.pl")
    password = factory.django.Password('test_pass321123')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    about = factory.Faker('text', max_nb_chars=800)


class LanguageFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Language

    language_pol = factory.Sequence(lambda x: f'jezyk_{x}')
    language_eng = factory.Sequence(lambda x: f'lang_{x}')
    symbol = factory.Sequence(lambda x: f'{x}tst'[:3])


class WordFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Word

    word = factory.Sequence(lambda x: f"word-{x*'t'}")
    language = factory.SubFactory(LanguageFactory)


class LinkFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Link

    user = factory.SubFactory(ImpUserFactory)
    base = factory.SubFactory(WordFactory)
    translation = factory.SubFactory(WordFactory)
    random_nr = 0
