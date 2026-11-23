from .repositories import HealthRepository
from .services import HealthService


def get_health_service() -> HealthService:
    return HealthService(
        health_repo=HealthRepository(),
    )