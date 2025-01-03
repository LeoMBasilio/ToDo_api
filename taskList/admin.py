from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'completed', 'created_at')
    list_display_links = ('id', 'title')
    list_per_page = 25
    search_fields = ('title', 'description')

admin.site.register(Task, TaskAdmin)
