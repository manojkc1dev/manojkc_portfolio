import uuid
from django.db import models

class BaseModel(models.Model):
    """
    Abstract base model providing primary key UUIDs, timestamps,
    and soft-delete capabilities across all apps.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True
        ordering = ['-created_at']