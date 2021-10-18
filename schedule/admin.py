from django.contrib import admin
from .models import Schedule

# Register your models here.

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'room_number')
    list_display_links = ('room_number',)
    search_fields = ('id', 'name', 'room_number')
    list_editable = ('name',)
    list_filter = ('id', 'name')


admin.site.register(Schedule, ScheduleAdmin)