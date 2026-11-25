from django.contrib.auth.base_user import BaseUserManager
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .custom_user import CustomUser


class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number: str, password: str | None = None, **extra_fields: Any) -> "CustomUser":
        if not password:
            raise ValueError("Users must have a password")
        if not phone_number:
            raise ValueError("Users must have a phone_number")
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number: str, password: str | None = None, **extra_fields: Any) -> "CustomUser":
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(phone_number, password, **extra_fields)
