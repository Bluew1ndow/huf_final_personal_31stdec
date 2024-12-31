from django.contrib import admin
from .models import join_us_table, share_experience_table, ask_suggestion_table
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin, ExportMixin
from .resources import *
class JoinUsAdmin(ImportExportModelAdmin):
    resource_class = JoinUsResources
    list_display = ("name","identity_verified")
    list_filter = ("identity_verified",)
    search_fields = ("name", "phone_number",)

class ShareExperienceAdmin(ImportExportModelAdmin):
    resource_class = ShareExperienceResources
    list_display = ("name","disease","email_address",)
    search_fields = (
        "name",
        "pk",
        "city",
        "state",
        "country",
        "email_address",
        "phone_number",
        "disease",
        "pathies"
    )

class AskSuggestionAdmin(ImportExportModelAdmin):
    resource_class = AskSuggeestionsResources
    list_display = ("name","email_address",)
    search_fields = (
        "name",
        "pk",
        "city",
        "state",
        "country",
        "email_address",
        "phone_number",
        "disease",
        "pathies"
    )

admin.site.register(join_us_table, JoinUsAdmin)
admin.site.register(share_experience_table, ShareExperienceAdmin)
admin.site.register(ask_suggestion_table, AskSuggestionAdmin)