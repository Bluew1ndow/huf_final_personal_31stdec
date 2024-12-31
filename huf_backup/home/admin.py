from django.contrib import admin
from .models import testimonial_table, video_table, key_value_table
from .resources import *
from import_export.admin import ImportExportModelAdmin, ExportMixin


class TestimonialAdmin(ImportExportModelAdmin):
    resource_class = TestimonialResource
    list_filter = ("show",)
    list_display = ("heading", "text", "name", "location")


class VideoAdmin(ImportExportModelAdmin):
    resource_class = VideoResource
    list_display = ("heading", "image", "ytplaylist_link")


class KeyValueAdmin(ImportExportModelAdmin):
    resource_class = KeyValueResource
    list_display = ("key", "value")


admin.site.register(testimonial_table, TestimonialAdmin)
admin.site.register(video_table, VideoAdmin)
admin.site.register(key_value_table, KeyValueAdmin)