from django.contrib import admin
from import_export.admin import ImportExportModelAdmin, ExportMixin
from .resources import *

class PathyAdmin(ImportExportModelAdmin):
    resource_class = PathyResources
    list_display = ("title", "show",)
    list_filter = ("show",)
    search_fields = ("title",)

class EffectiveAdmin(ImportExportModelAdmin):
    resource_class = EffectiveResources
    list_display = ("name", "pathy","show")
    list_filter = ("show","pathy")
    search_fields = ("name",)

admin.site.register(pathy_table, PathyAdmin)
admin.site.register(effective_table, EffectiveAdmin)