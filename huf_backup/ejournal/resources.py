from import_export import resources, fields
from .models import (
    ejournal_table,
    subscription_table,
    key_value_table,
)


class EjournalResource(resources.ModelResource):
    class Meta:
        model = ejournal_table
        fields = ('id', 'name', 'image', 'file', 'show', 'publish_date','created_at', 'modified_at')


class SubscriptionResource(resources.ModelResource):
    class Meta:
        model = subscription_table
        fields = ('id', 'email_address', 'send','created_at', 'modified_at')


class KeyValueResource(resources.ModelResource):
    class Meta:
        model = key_value_table
        fields = ('id', 'key', 'value','created_at', 'modified_at')