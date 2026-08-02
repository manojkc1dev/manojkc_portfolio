from django.db.models import QuerySet
from .models import Experience

def get_all_experiences() -> QuerySet[Experience]:
    """Returns all non-deleted work experience entries ordered by display order."""
    return Experience.objects.filter(is_deleted=False).order_by('display_order', '-start_date')