from import_export import resources
from .models import donation_table

class DonationResource(resources.ModelResource):
    class Meta:
        model = donation_table
        fields = ('id', 'email_address', 'donation_amount', 'phone_number', 'address', 'message', 'receive_updates', 'created_at', 'stripe_id')
        export_order = ('id', 'email_address', 'donation_amount', 'phone_number', 'address', 'message', 'receive_updates', 'created_at', 'stripe_id')
