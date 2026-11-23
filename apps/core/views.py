from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from .container import get_health_service
from .schemas import get_health_schema


class HealthResponseView(APIView):
    permission_classes = [AllowAny]

    @get_health_schema
    def get(self, request: Request) -> Response:
        service = get_health_service()
        data, status_code = service.get_system_health()
        return Response(data, status=status_code)
