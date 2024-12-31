from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from .models import (
    effective_table,
    pathy_table,
)
class EffectiveResources(resources.ModelResource):
    pathy = fields.Field(
        column_name='pathy',
        attribute='pathy',
        widget=ForeignKeyWidget(pathy_table, field='title')
    )
    class Meta:
        model = effective_table
        fields = ('id','pathy','name','link','show','created_at','modified_at')

class PathyResources(resources.ModelResource):
    class Meta:
        model = pathy_table
        fields = ('id','title','text','image','show','created_at','modified_at')

