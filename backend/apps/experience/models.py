from django.db import models
from core.models import BaseModel

class Experience(BaseModel):
    company_name = models.CharField(max_length=150)
    role_title = models.CharField(max_length=150)
    location = models.CharField(max_length=100, default="Remote / Kathmandu")
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True, help_text="Leave blank if current role")
    is_current = models.BooleanField(default=False)
    description = models.TextField(help_text="Key responsibilities and achievements")
    technologies_used = models.CharField(max_length=250, help_text="Comma-separated list (e.g., Python, Django, React)")
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = "Experience Records"
        ordering = ['display_order', '-start_date']

    def __str__(self):
        return f"{self.role_title} at {self.company_name}"