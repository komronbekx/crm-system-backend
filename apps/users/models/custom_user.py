from apps.core.models import BaseModel
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from apps.core.validators import phone_validator
from .center import Center
from .custom_user_manager import CustomUserManager


class UserRole(models.TextChoices):
    DIRECTOR = "DIRECTOR"
    ADMIN = "ADMIN"
    TEACHER = "TEACHER"
    ACCOUNTANT = "ACCOUNTANT"


class CustomUser(AbstractBaseUser, PermissionsMixin, BaseModel):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13, unique=True, validators=[phone_validator])
    role = models.CharField(max_length=11, choices=UserRole.choices, blank=True, null=True)
    center = models.ForeignKey(Center, on_delete=models.PROTECT, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ["full_name"]

    def __str__(self) -> str:
        return f"{self.full_name}"
