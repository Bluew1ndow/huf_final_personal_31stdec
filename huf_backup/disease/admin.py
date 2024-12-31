from django.contrib import admin
from import_export.admin import ImportExportModelAdmin, ExportMixin
from .resources import *



class DiseaseAdmin(ImportExportModelAdmin):
    resource_class = DiseaseResource
    list_filter = ("show",)
    search_fields = ("name",)



class PathyAdmin(ImportExportModelAdmin):           # Modified admin.ModelAdmin -> ImportExportAdmin
    resource_class = PathyResource                  # PathyResource Class Imported from resources.py
    list_filter = ("disease__name", "show")
    search_fields = ("name",)



class DataAdmin(ImportExportModelAdmin):
    resource_class = DataResource
    list_display = ("title","pk","pathy","source",)
    list_filter = ("pathy__disease","pathy__name","source","show",)
    search_fields = ("title","pk",)


class SourceAdmin(ImportExportModelAdmin):
    resource_class = SourceResource
    search_fields = ("title","pk")


class CaseAdmin(ImportExportModelAdmin):
    resource_class = CaseResource
    list_display = ("title","pk",)
    list_filter = ("pathy__disease","pathy__name","show",)
    search_fields = ("pk", "title", "first_name", "last_name")


class SexAdmin(ImportExportModelAdmin):
    resource_class = SexResource
    list_filter = ("show",)


class BookAdmin(ImportExportModelAdmin):
    resource_class = BookResource
    list_display = ("name","author","rating")
    list_filter = ("pathy__disease","pathy__name","show",)
    search_fields = ("name","author",)


class WhatsappAdmin(ImportExportModelAdmin):
    resource_class = WhatsappResource
    list_display = ("pathy",)
    list_filter = ("pathy__disease","pathy__name","show",)
    search_fields = ("pathy__name",)

class SummaryAdmin(ImportExportModelAdmin):
    resource_class = SummaryResource
    list_display = ("pathy",)
    list_filter = ("pathy__disease","pathy__name",)
    search_fields = ("pathy__name",)


admin.site.register(disease_table, DiseaseAdmin)
admin.site.register(pathy_table, PathyAdmin)
admin.site.register(data_table, DataAdmin)
admin.site.register(source_table, SourceAdmin)
admin.site.register(case_table, CaseAdmin)
admin.site.register(sex_table, SexAdmin)
admin.site.register(book_table, BookAdmin)
admin.site.register(whatsapp_table, WhatsappAdmin)
admin.site.register(summary_table, SummaryAdmin)