import uuid

from django.db import connection, models
from django.db.models.query import QuerySet
from django.db.utils import OperationalError, DatabaseError
from typing import TypeVar, Generic, Any

T = TypeVar('T', bound=models.Model)


class HealthRepository:
    def check_database(self) -> bool:
        try:
            with connection.cursor() as cursor:
                cursor.execute('SELECT 1;')
            return True
        except (OperationalError, DatabaseError):
            return False


class BaseRepository(Generic[T]):
    model: type[T]

    def get_by_id(self, id: uuid.UUID) -> T | None:
        return self.model.objects.filter(id=id).first()

    def list_all(self) -> QuerySet[T]:
        return self.model.objects.all()

    def create(self, **kwargs: Any) -> T:
        return self.model.objects.create(**kwargs)

    def update(self, instance: T, **kwargs: Any) -> T:
        for attr, value in kwargs.items():
            setattr(instance, attr, value)
        instance.save(update_fields=list(kwargs.keys()) + ['updated_at'])
        return instance

    def delete(self, instance: T) -> None:
        instance.delete()
