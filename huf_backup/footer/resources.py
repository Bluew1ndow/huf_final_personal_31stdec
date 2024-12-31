from import_export import resources, fields
from .models import (
    footer_table
)


class FooterResource(resources.ModelResource):
    class Meta:
        model = footer_table
        fields = ('id', 'key', 'value', "created_at", "modified_at")