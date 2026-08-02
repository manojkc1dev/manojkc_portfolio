# apps/hero/models.py
from django.db import models
from core.models import BaseModel

class Hero(BaseModel):
    full_name = models.CharField(max_length=150)
    professional_title = models.CharField(max_length=200)
    headline = models.CharField(max_length=300)
    short_introduction = models.TextField()
    profile_photo = models.ImageField(upload_to='hero/')
    resume_pdf = models.FileField(upload_to='hero/resume/', blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    email = models.EmailField()
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Hero Section"

    def __str__(self):
        return f"Hero Content - {self.full_name}"