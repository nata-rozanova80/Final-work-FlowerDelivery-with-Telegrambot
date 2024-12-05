from django.db import models
from flowerdelivery.catalog.models import Products, CustomUser


class Orders (models.Model):
    order_id = models.ForeignKey('self', on_delete=models.CASCADE, null=False, blank=False)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=False, blank=False)
    products_id = models.ForeignKey(Products, on_delete=models.CASCADE,null=False, blank=False)
    status = models.CharField(max_length=20, choices=[('NEW', 'New'), ('IN_PROGRESS', 'In Progress'), ('DONE', 'Done')])
    order_sum = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)

