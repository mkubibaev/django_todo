from django.contrib import admin
from django.urls import path

from webapp.views import index_view, todo_add_view, todo_view, todo_edit_view, todo_delete_view

urlpatterns = [
    path('', index_view, name='index'),
    path('todo/add', todo_add_view, name='todo_add'),
    path('todo/<int:pk>', todo_view, name='todo'),
    path('todo/<int:pk>/edit', todo_edit_view, name='todo_edit'),
    path('todo/<int:pk>/delete', todo_delete_view, name='todo_delete'),
    path('admin/', admin.site.urls),
]
