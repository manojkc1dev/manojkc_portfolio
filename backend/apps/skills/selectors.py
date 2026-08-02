from django.db.models import QuerySet
from .models import Skill

def get_all_skills() -> QuerySet[Skill]:
    """Returns all non-deleted skills ordered by display order."""
    return Skill.objects.filter(is_deleted=False).order_by('display_order', 'name')