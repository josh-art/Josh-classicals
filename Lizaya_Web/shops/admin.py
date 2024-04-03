from django.contrib import admin
from django.contrib import admin
from .models import Category, Contacts


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Contacts)

# Register your models here.
