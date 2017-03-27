from django.contrib import admin
from .models import Event

@admin.register(Event)
class AdminMember(admin.ModelAdmin):
    list_display = ('date_start', 'date_end', 'title',
                    'description', 'location', 'timezone',
                    'organizer', 'email' )
    list_filter = ('organizer',)
