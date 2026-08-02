from .models import Hero

def get_active_hero() -> Hero | None:
    """Returns the currently active hero section profile."""
    return Hero.objects.filter(is_deleted=False, is_active=True).first()