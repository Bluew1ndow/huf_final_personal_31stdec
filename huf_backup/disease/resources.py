from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from .models import (
    disease_table,
    pathy_table,
    summary_table,
    data_table,
    source_table,
    case_table,
    sex_table,
    book_table,
    whatsapp_table,
)



class DiseaseResource(resources.ModelResource):
    class Meta:
        model = disease_table
        fields = ('id','name','show','text','summary','image_link','created_at','modified_at')

class PathyResource(resources.ModelResource):
    disease = fields.Field(
        column_name='disease',
        attribute='disease',
        widget=ForeignKeyWidget(disease_table, field='name')
    )

    class Meta:
        model = pathy_table
        fields = ('id','disease','name','show','type','created_at','modified_at')

class SourceResource(resources.ModelResource):
    class Meta:
        model = source_table
        fields = ('id','name','text','show','created_at','modified_at')

class SexResource(resources.ModelResource):
    class Meta:
        model = sex_table
        fields = ('id','sex','show','created_at','modified_at')

class BookResource(resources.ModelResource):
    pathy = fields.Field(
        column_name='pathy',
        attribute='pathy',
        widget=ForeignKeyWidget(pathy_table, 'name')
    )

    disease = fields.Field(
        column_name='disease'
    )

    def dehydrate_disease(self, obj):
        # Directly access the related field
        return obj.pathy.disease.name if obj.pathy and obj.pathy.disease else ''

    class Meta:
        model = book_table
        fields = (
            'id', 'pathy', 'show', 'name', 'author', 'rating', 'text',
            'image_link', 'buy_link', 'disease', 'created_at', 'modified_at'
        )


class SummaryResource(resources.ModelResource):
    pathy = fields.Field(
        column_name='pathy',
        attribute='pathy',
        widget=ForeignKeyWidget(pathy_table, field='name')
    )

    disease = fields.Field(
        column_name='disease'
    )

    def dehydrate_disease(self, obj):
        return obj.pathy.disease.name if obj.pathy and obj.pathy.disease else ''

    class Meta:
        model = summary_table
        fields = ('id','pathy','summary','created_at','modified_at')

class DataResource(resources.ModelResource):
    pathy = fields.Field(
        column_name='pathy',
        attribute='pathy',
        widget=ForeignKeyWidget(pathy_table, field='name')
    )

    source = fields.Field(
        column_name='source',
        attribute='source',
        widget=ForeignKeyWidget(data_table, field='name')
    )

    disease = fields.Field(
        column_name='disease'
    )

    def dehydrate_disease(self, obj):
        return obj.pathy.disease.name if obj.pathy and obj.pathy.disease else ''

    class Meta:
        model = book_table
        fields = ('id', 'pathy', 'disease','source', 'show', 'title','link','summary','rating','comment','created_at','modified_at')

class CaseResource(resources.ModelResource):
    pathy = fields.Field(
        column_name='pathy',
        attribute='pathy',
        widget=ForeignKeyWidget(pathy_table, field='name')
    )

    sex = fields.Field(
        column_name='sex',
        attribute='sex',
        widget=ForeignKeyWidget(sex_table, field='sex')
    )

    disease = fields.Field(
        column_name='disease'
    )

    def dehydrate_disease(self, obj):
        return obj.pathy.disease.name if obj.pathy and obj.pathy.disease else ''

    class Meta:
        model = case_table
        fields = ('id', 'pathy', 'disease', 'title', 'summary', 'rating', 'comment',
                  'first_name', 'last_name', 'sex', 'age', 'occupation', 'email_address',
                  'phone_number', 'street_address', 'zip_code', 'state', 'country',
                  'history_link', 'allergies_link', 'reports_link', 'show', 'show_name',
                  'show_email', 'show_phone_number', 'show_address', 'created_at', 'modified_at')

class WhatsappResource(resources.ModelResource):
    pathy = fields.Field(
        column_name='pathy',
        attribute='pathy',
        widget=ForeignKeyWidget(pathy_table, field='name')
    )

    disease = fields.Field(
        column_name='disease'
    )

    def dehydrate_disease(self, obj):
        return obj.pathy.disease.name if obj.pathy and obj.pathy.disease else ''

    class Meta:
        model = whatsapp_table
        fields = ('id','pathy','disease','link','show','created_at','modified_at')

