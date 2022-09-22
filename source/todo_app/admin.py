from django.contrib import admin

from todo_app.models import Task

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ("id","title", "description", "status", "deadline", "created_at")
    list_filter = ("id", "title", "description", "status", "deadline", "created_at")
    search_fields = ("title", "description", "status")
    fields = ("title", "description", "status", "deadline", "created_at", "changed_at")
    readonly_fields = ("id", "created_at", "changed_at")

admin.site.register(Task, TaskAdmin)