from django.db import models
from simple_history.models import HistoricalRecords

# Create your models here.
class donation_table(models.Model):
    email_address = models.CharField(max_length=1000)
    donation_amount = models.FloatField()
    phone_number = models.CharField(max_length=1000)
    address = models.CharField(max_length=1000)
    message = models.CharField(max_length=1000, blank=True, null=True)
    receive_updates = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    stripe_id = models.CharField(max_length=1000, default="####")
    history = HistoricalRecords()

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.email_address


