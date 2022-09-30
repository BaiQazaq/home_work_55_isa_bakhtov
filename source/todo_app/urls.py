from django.urls import path

from todo_app.views.base import base_view
from todo_app.views.tasks_methods import add_view, detail_view, update_view

urlpatterns = [
    path("", base_view, name='base'),
    path("tasks/add/", add_view, name='creation'),
    path("task/<int:pk>/update/", update_view, name='update'),
    path("task/<int:pk>", detail_view, name='show')
]