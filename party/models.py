from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    country = models.CharField(max_length=100)
    customer_type = models.CharField(max_length=50)
    interested_items = models.JSONField(default=list)

    is_deleted = models.BooleanField(default=False)   # 👈 NEW FIELD

    def __str__(self):
        return self.name

