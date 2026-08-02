from django.db import models
from core.models import BaseModel

class Project(BaseModel):
    class StatusChoices(models.TextChoices):
        DRAFT = 'DR', 'Draft'
        PUBLISHED = 'PB', 'Published'
        ARCHIVED = 'AR', 'Archived'

    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    short_description = models.CharField(max_length=500)
    full_description = models.TextField()
    thumbnail = models.ImageField(upload_to='projects/thumbnails/', blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    live_demo_url = models.URLField(blank=True, null=True)
    status = models.CharField(
        max_length=2, 
        choices=StatusChoices.choices, 
        default=StatusChoices.DRAFT
    )
    is_featured = models.BooleanField(default=False)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['display_order', '-created_at']

    def __str__(self):
        return self.title