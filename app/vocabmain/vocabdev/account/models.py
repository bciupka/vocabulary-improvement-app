from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from ..improver.models import Language
from django.core.exceptions import ValidationError


class ImpUserManager(BaseUserManager):

    def create_user(self, username, email, password, **additional_fields):
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **additional_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password, **additional_fields):
        additional_fields.setdefault('is_staff', True)
        additional_fields.setdefault('is_active', True)
        additional_fields.setdefault('is_superuser', True)

        if additional_fields.get('is_superuser') is not True or additional_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to superuser and stuff')

        return self.create_user(username, email, password, **additional_fields)


class ImpUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(_('email address'), max_length=150, unique=True)
    first_name = models.CharField(_('first name'), max_length=150, blank=True, null=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True, null=True)
    start_date = models.DateTimeField(default=timezone.now)
    fav_language = models.ForeignKey(Language, on_delete=models.SET_NULL, blank=True, null=True)
    about = models.TextField(_('about section'), max_length=800, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = ImpUserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def __str__(self):
        return f'{self.username}'

    def save(self, *args, **kwargs):
        if not self.fav_language:
            try:
                language = Language.objects.get(symbol='eng')
            except Language.DoesNotExist:
                language = None
            self.fav_language = language
        super().save(*args, **kwargs)
