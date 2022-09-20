from django.contrib import admin

from todo_app.models import Task

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "description", "status", "deadline", "created_at")
    list_filter = ("id", "description", "status", "deadline", "created_at")
    search_fields = ("description", "status")
    fields = ("description", "status", "deadline", "created_at", "changed_at")
    readonly_fields = ("id", "created_at", "changed_at")

admin.site.register(Task, TaskAdmin)