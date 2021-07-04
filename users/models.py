import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db.models import signals
from .tasks import send_verification_email


class UserAccountManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email address must be provided')

        if not password:
            raise ValueError('Password must be provided')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields['is_staff'] = True
        extra_fields['is_superuser'] = True

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    objects = UserAccountManager()

    email = models.EmailField('Электронная почта', unique=True, blank=False, null=False)
    full_name = models.CharField('Пользователь', blank=False, null=True, max_length=400)
    is_staff = models.BooleanField('Cтатус персонала', default=False)
    is_active = models.BooleanField('Активный?', default=True)
    is_verified = models.BooleanField('Подтверждён?', default=False)  # Add the `is_verified` flag
    verification_uuid = models.UUIDField('Уникальный UUID проверки', default=uuid.uuid4)

    def get_short_name(self):
        return self.email

    def get_full_name(self):
        return self.email

    def __unicode__(self):
        return self.email

    def __str__(self):
        return "{0}; Почта - {1}".format(self.full_name, self.email)

    class Meta:
        ordering = ['-is_active', '-is_verified', '-full_name']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

def user_post_save(sender, instance, signal, *args, **kwargs):
    if not instance.is_verified:
        send_verification_email(instance.pk)


# signals.post_save.connect(user_post_save, sender=User)