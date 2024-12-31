from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from .models import (
    members_table,
key_value_table,
)


class MembersResources(resources.ModelResource):
    class Meta:
        model = members_table
        fields = ('id','name','show','image','designation','about','team','linkedin_url','email_address','phone_number','show','created_at','modified_at')
class KeyResources(resources.ModelResource):
    class Meta:
        model = key_value_table
        fields = ('id','key','value','created_at','modified_at')