from django.db import models

class Customer(models.Model):

    CUSTOMER_TYPE_CHOICES = [
        ('regular', 'Regular'),
        ('premium', 'Premium'),
        ('vip', 'VIP'),
    ]

    ITEM_CHOICES = [
        ('lights', 'Lights'),
        ('sound', 'Sound System'),
        ('decoration', 'Decoration'),
        ('catering', 'Catering'),
    ]

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    country = models.CharField(max_length=50)

    customer_type = models.CharField(
        max_length=20,
        choices=CUSTOMER_TYPE_CHOICES
    )

    interested_items = models.JSONField()  # Stores multiple checkbox values

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
