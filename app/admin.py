from django.contrib import admin

from app.models.projects import Stage
from app.models.projects import Order


@admin.register(Stage)
class StageAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = ['name', 'stage', 'created_at', 'deadline', 'completed']
    list_filter = ['stage']
