from django.db import models

class Hero(models.Model):
    name = models.CharField(max_length=100, default="MANOJ K.C.")
    availabilityBadge = models.CharField(max_length=255, default="Available for On-Site (Kathmandu) & Remote Roles")
    typingTexts = models.TextField(default="Python & Django Backend Architect,FinTech Systems Integrator")
    subtitle = models.CharField(max_length=255, default="REST APIs • Microservices • PostgreSQL • JWT Auth")
    description = models.TextField(default="Specialized in architecting high-throughput REST APIs, resilient relational database schemas, and secure transaction pipelines.")
    location = models.CharField(max_length=100, default="Kathmandu, Nepal")
    hireMeUrl = models.CharField(max_length=255, default="#contact")
    profileImage = models.CharField(max_length=255, default="/profile.jpg")
    
    full_name = models.CharField(max_length=100, default="MANOJ K.C.")
    professional_title = models.CharField(max_length=255, default="Python & Django Backend Architect")
    email = models.EmailField(default="manoj@example.com")
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name