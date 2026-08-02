from django.db.models import QuerySet
from .models import Project

def get_published_projects() -> QuerySet[Project]:
    """
    Returns only projects that are published and not soft-deleted,
    ordered by their display order.
    """
    return Project.objects.filter(
        is_deleted=False, 
        status=Project.StatusChoices.PUBLISHED
    ).order_by('display_order', '-created_at')