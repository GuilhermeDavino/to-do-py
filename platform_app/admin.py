from django.contrib import admin

from platform_app.models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display_links = ['id']
    list_display = ('id', 'title', 'description', 'status')
    list_editable = ('title', 'description', 'status')
    search_fields = ('title', 'status')
    list_filter = ('title', 'status')

