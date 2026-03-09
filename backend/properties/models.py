from django.db import models
from users.models import User


class Property(models.Model):
    PROPERTY_TYPE_CHOICES = [
        ('apartment', 'Apartment'),
        ('house', 'House'),
        ('condo', 'Condo'),
        ('villa', 'Villa'),
        ('studio', 'Studio'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    square_feet = models.FloatField()
    property_type = models.CharField(max_length=50, choices=PROPERTY_TYPE_CHOICES)

    price_per_month = models.DecimalField(max_digits=10, decimal_places=2)
    available_from = models.DateField()
    is_available = models.BooleanField(default=True)

    main_image = models.ImageField(upload_to='properties/', blank=True, null=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='properties')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    rating = models.FloatField(default=0)

    class Meta:
        db_table = 'properties'
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'

    def __str__(self):
        return self.title