from django.contrib import admin
from import_export.admin import ImportExportModelAdmin, ExportMixin
from .resources import *


class MembersAdmin(ImportExportModelAdmin):
    resource_file=MembersResources
    list_display = ("name","team",)
    search_fields = ("name",)
    list_filter = ("show","team")

class Key_valueAdmin(ImportExportModelAdmin):
    resource_file=KeyResources
    list_display = ("key","value",)




admin.site.register(members_table, MembersAdmin)
admin.site.register(key_value_table,Key_valueAdmin)

