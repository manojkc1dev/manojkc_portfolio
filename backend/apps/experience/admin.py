from django.contrib import admin
from .models import Experience

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('role_title', 'company_name', 'start_date', 'is_current', 'display_order')
    list_editable = ('is_current', 'display_order')
    list_filter = ('is_current',)
    search_fields = ('company_name', 'role_title')