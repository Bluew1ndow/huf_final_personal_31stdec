from import_export import resources, fields
from .models import (
    clinics_table
)

class ClinicsResource(resources.ModelResource):
    class Meta:
        model = clinics_table
        fields = ('id', 'name', 'image', 'summary', 'locationLink', 'contact','tags', 'show','created_at', 'modified_at')

