from .repositories import HealthRepository


class HealthService:
    def __init__(self, health_repo: HealthRepository) -> None:
        self.health_repo = health_repo

    def get_system_health(self) -> tuple[dict, int]:
        is_db_ok = self.health_repo.check_database()
        if is_db_ok:
            return {"status": "ok"}, 200
        return {"status": "error"}, 503
