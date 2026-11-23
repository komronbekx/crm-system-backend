from django.urls import path
from .views import HealthResponseView

urlpatterns = [
    path('health/', HealthResponseView.as_view(), name='health'),
]
