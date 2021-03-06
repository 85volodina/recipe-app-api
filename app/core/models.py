from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin

class UserManager (BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError("Users must have email address")
        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user=self.create_user(email, password)
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)

        return user


class User(AbstractUser, PermissionsMixin):
    """Custom User model, that supports email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)

    objects = UserManager()
    REQUIRED_FIELDS = []

    USERNAME_FIELD = 'email'


