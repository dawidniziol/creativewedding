from django.contrib import admin

from app.models.projects import Stage
from app.models.projects import Order
from app.models.projects import Offers


@admin.register(Stage)
class StageAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = ['name',
                    'stage',
                    'deadline_invitations',
                    'completed_invitations',
                    'angels_extras',
                    'deadline_extras',
                    'completed_extras']

    list_filter = ['completed_invitations',
                   'completed_extras',
                   'stage', ]

@admin.register(Offers)
class OfferAdmin(admin.ModelAdmin):
    list_display = ['name', 'samples', ]