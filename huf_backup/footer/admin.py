from django.contrib import admin
from .resources import *
from import_export.admin import ImportExportModelAdmin, ExportMixin

class FooterAdmin(ImportExportModelAdmin):
    resource_class = FooterResource
    list_display = ("key", "value",)

admin.site.register(footer_table, FooterAdmin)