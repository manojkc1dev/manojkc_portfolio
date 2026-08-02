from django.db import models
from core.models import BaseModel

class Skill(BaseModel):
    class CategoryChoices(models.TextChoices):
        LANGUAGE = 'LANG', 'Programming Language'
        FRAMEWORK = 'FW', 'Framework / Library'
        DATABASE = 'DB', 'Database'
        DEVOPS = 'DEV', 'DevOps & Cloud'
        TOOL = 'TOOL', 'Tools & Version Control'

    name = models.CharField(max_length=100, unique=True)
    category = models.CharField(max_length=10, choices=CategoryChoices.choices)
    percentage = models.PositiveIntegerField(help_text="Proficiency percentage (e.g., 90)")
    experience_years = models.CharField(max_length=50, blank=True, null=True, help_text="e.g., '3+ Years'")
    is_featured = models.BooleanField(default=False)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['display_order', 'name']

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"