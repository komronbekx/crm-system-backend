from django.db import connection
from django.db.utils import OperationalError, DatabaseError


class HealthRepository:
    def check_database(self) -> bool:
        try:
            with connection.cursor() as cursor:
                cursor.execute('SELECT 1;')
            return True
        except (OperationalError, DatabaseError):
            return False
