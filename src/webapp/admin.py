from django.contrib import admin
from webapp.models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ['description', 'status', 'date']


admin.site.register(Todo, TodoAdmin)
