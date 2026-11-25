from django.contrib import admin
from apps.users.models import Center


@admin.register(Center)
class CenterAdmin(admin.ModelAdmin):
    list_display = ("name", "phone_number", "address", "is_active")
    search_fields = ("name", "phone_number")
    list_filter = ("is_active",)
