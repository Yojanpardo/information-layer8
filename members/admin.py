from django.contrib import admin
from .models import Member

@admin.register(Member)
class AdminEvent(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'phone', 'email', 'address',
                    'personal_skills', 'team_skills', 'weakness',
                    'under_presure',)
    list_filter = ('email',)
