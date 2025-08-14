from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
        USER_TYPE_CHOICES = (
                ('patient', 'Patient'),
                ('doctor', 'Doctor'),
        )

        user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='patient')
        profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
        address_line1 = models.CharField(max_length=255)
        city = models.CharField(max_length=200)
        state = models.CharField(max_length=200)
        pincode = models.CharField(max_length=6)

        def __str__(self):
                return self.username