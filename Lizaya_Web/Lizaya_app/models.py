from django.db import models
from django.db import models
from django.utils import timezone
from django.urls import reverse


class Contacts(models.Model):
    user_name = models.CharField(max_length=200, blank=False)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=20, blank=True, null=True)
    message = models.TextField(max_length=300)
    submitted_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('submitted_date',)

    def __str__(self):
        return self.user_name

    pass



class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='author')
    image = models.ImageField(blank=True, null=False, upload_to='post_pics')
    body = models.TextField(blank=True)
    caption = models.CharField(max_length=500)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.caption

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})



# Create your models here.
