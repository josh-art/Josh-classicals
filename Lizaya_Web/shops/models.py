from django.db import models
from django.urls import reverse
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=15, db_index=True)
    slug = models.SlugField(max_length=15, unique=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shops:product_list_by_category', args=[self.slug])



class Contacts(models.Model):
    user_name = models.CharField(max_length=20, blank=False)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=20, blank=True, null=True)
    message = models.TextField(max_length=100)
    submitted_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('submitted_date',)

    def __str__(self):
        return self.user_name

    pass


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='media/%Y/%m/%d', blank=True)

    class Meta:
        ordering = ('name', )
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shops:product_detail', args=[self.id, self.slug])

class ProductFeatured(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, null=True, blank=True)
    text = models.CharField(max_length=220, null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.product.name


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=120, null=True, blank=True)
    email = models.EmailField()
    FIVE = '5'
    FOUR = '4'
    THREE = '3'
    TWO = '2'
    ONE = '3'
    NUM = (
        (FIVE, '5'),
        (FOUR, '4'),
        (THREE, '3'),
        (TWO, '2'),
        (ONE, '1')
    )
    stars = models.CharField(max_length=100, choices=NUM, default=FIVE)
    caption = models.CharField(max_length=120, null=True, blank=True)
    review = models.TextField()
    active = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name

# Create your models here.
