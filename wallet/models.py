import uuid

from django.db import models
from django.utils import timezone

from customer.models import Customer


class Wallet(models.Model):
    id = models.BigAutoField(primary_key=True)
    wxid = models.UUIDField(unique=True, default=uuid.uuid4)
    customer = models.ForeignKey(Customer, blank=False, null=False, on_delete=models.CASCADE, db_column='cxid')
    status = models.BooleanField(default=False)
    enabled_at = models.DateTimeField(default=timezone.now)
    balance = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'wallet'

    def get_dict(self):
        dict_obj = {'wallet_id': self.wxid if self.wxid else None,
                    'customer_id': self.customer.cxid if self.customer.cxid else None
                    }
        return dict_obj
