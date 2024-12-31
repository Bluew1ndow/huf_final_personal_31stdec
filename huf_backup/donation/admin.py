from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import donation_table
from .resources import DonationResource

class DonationAdmin(ImportExportModelAdmin):
    resource_class = DonationResource
    list_filter = ('receive_updates',)  # Filter donations by whether updates are received
    search_fields = ('email_address', 'phone_number', 'address')  # Make these fields searchable

admin.site.register(donation_table, DonationAdmin)
