from django.contrib import admin
from .models import Hero

@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'professional_title', 'email', 'is_active', 'updated_at')
    list_editable = ('is_active',)