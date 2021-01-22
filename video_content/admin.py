"""
Possibility to add sth. to Admin Interface out of this APP: video_content
"""
from django.contrib import admin

# pylint: disable = import-error, relative-beyond-top-level
from .models import Video, Timestamp


admin.site.register(Video)


@admin.register(Timestamp)
class TimestampAdmin(admin.ModelAdmin):
    list_display = ('video', 'building', 'time')
