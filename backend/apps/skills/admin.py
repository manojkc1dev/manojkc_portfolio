from django.contrib import admin
from .models import Skill

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'percentage', 'experience_years', 'is_featured', 'display_order')
    list_editable = ('percentage', 'is_featured', 'display_order')
    list_filter = ('category', 'is_featured')
    search_fields = ('name',)