from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'is_featured', 'display_order', 'created_at')
    list_editable = ('status', 'is_featured', 'display_order')
    list_filter = ('status', 'is_featured')
    search_fields = ('title', 'short_description')
    prepopulated_fields = {'slug': ('title',)} # Auto-generates the slug from the title