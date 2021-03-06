from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class MyDispatcherManager(BaseUserManager):

    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Диспетчер должен иметь email!')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Dispatcher(AbstractBaseUser):
    username = models.CharField(
        verbose_name="Имя",
        max_length=50
    )

    phone_number = PhoneNumberField(
        verbose_name='Номер телефона',
        blank=True
    )

    email = models.EmailField(
        verbose_name='Email-адрес',
        max_length=50,
        unique=True
    )

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyDispatcherManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Диспетчер'
        verbose_name_plural = 'Список диспетчеров'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin