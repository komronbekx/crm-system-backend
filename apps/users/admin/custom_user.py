from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import BaseUserCreationForm, UserChangeForm

from apps.users.models import CustomUser


class CustomUserCreationForm(BaseUserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("full_name", "phone_number", "role", "center")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("full_name", "phone_number", "role", "center", "is_active")


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ('full_name', 'phone_number', 'role', 'center', 'is_active')
    search_fields = ("full_name", "phone_number")
    ordering = ("full_name",)
    fieldsets = (("Entry fields", {"fields": ("phone_number", "password")}),
                 ("Personal info", {"fields": ("full_name",)}),
                 ("Company info", {"fields": ("center", "role")}),
                 ("Law info", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")},))
    add_fieldsets = ((None, {"fields": ("phone_number", "full_name", "role", "center", "password1", "password2")}),)
