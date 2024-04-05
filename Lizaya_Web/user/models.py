from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(default=0)
    phone = models.CharField(max_length=14)
    cover_photos = models.ImageField(default='cover3.jpeg', upload_to='cover_pics')
    stripe_customer_id = models.CharField(max_length=50, blank=True, null=True)
    one_click_purchasing = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.username} Profile'

