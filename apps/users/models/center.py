from django.db import models
from apps.core.models import BaseModel
from apps.core.validators import phone_validator


class Center(BaseModel):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13, validators=[phone_validator], unique=True, blank=True, null=True)
    address = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name
