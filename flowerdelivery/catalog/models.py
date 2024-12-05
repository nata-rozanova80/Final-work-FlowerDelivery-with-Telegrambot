from django.db import models


class Products(models.Model):
    product_id = models.ForeignKey('self', on_delete=models.CASCADE, null=False, blank=False)
    product = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='img/')
    description = models.TextField(blank=True)
    

# Пример записи ключа user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
class CustomUser:
    pass