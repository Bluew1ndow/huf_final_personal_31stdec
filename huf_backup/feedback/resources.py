from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from .models import (
    feedback_table
)

class FeedbackResource(resources.ModelResource):
    class Meta:
        model = feedback_table
        fields = ('id','rating','feedback','created_at','modified_at')