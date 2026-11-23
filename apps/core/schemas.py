from drf_spectacular.utils import extend_schema
from .serializers import HealthResponseSerializer

get_health_schema = extend_schema(
    summary="Health endpoint",
    description="Server va ma'lumotlar bazasi holatini tekshiradi",
    responses={200: HealthResponseSerializer,
               503: HealthResponseSerializer
               },
    tags=["health"]
)
