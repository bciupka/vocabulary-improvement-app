import pytest
from vocabdev.account.models import ImpUser

pytestmark = pytest.mark.django_db

class TestImpUserModel:
    def test_str_method(self, imp_user_factory):
        obj = imp_user_factory(username='test_user')
        assert str(obj) == 'test_user'

    def test_save_method(self, imp_user_factory, language_factory):
        lang = language_factory(symbol='pol')
        obj1 = imp_user_factory()
        language_factory(symbol='eng')
        obj2 = imp_user_factory()
        obj3 = imp_user_factory(fav_language=lang)
        assert obj1.fav_language is None
        assert obj2.fav_language.symbol == 'eng'
        assert obj3.fav_language.symbol == 'pol'


class TestImpUserManager:
    def test_create_user(self, imp_user_factory):
        imp_user = imp_user_factory(
            username="testuser",
            email="testuser@example.com",
            password="testpassword",
            first_name="Test",
            last_name="User",
            about="I am a test user"
        )

        assert imp_user.username == "testuser"
        assert imp_user.email == "testuser@example.com"
        assert imp_user.first_name == "Test"
        assert imp_user.last_name == "User"
        assert imp_user.about == "I am a test user"
        assert imp_user.check_password("testpassword")

    def test_create_superuser(self):
        obj = ImpUser.objects.create_superuser(
            username="testsuperuser",
            email="testsuperuser@example.com",
            password="testpassword",
            first_name="Test",
            last_name="Superuser",
            about="I am a test superuser"
        )

        assert obj.is_superuser
        assert obj.is_staff

    def test_create_superuser_is_superuser_is_staff_false(self):
        with pytest.raises(ValueError, match="Superuser must be assigned to superuser and stuff"):
            ImpUser.objects.create_superuser(
                username="testsuperuser",
                email="testsuperuser@example.com",
                password="testpassword",
                first_name="Test",
                last_name="Superuser",
                about="I am a test superuser",
                is_superuser=False
            )

        with pytest.raises(ValueError, match="Superuser must be assigned to superuser and stuff"):
            ImpUser.objects.create_superuser(
                username="testsuperuser",
                email="testsuperuser@example.com",
                password="testpassword",
                first_name="Test",
                last_name="Superuser",
                about="I am a test superuser",
                is_staff=False
            )
