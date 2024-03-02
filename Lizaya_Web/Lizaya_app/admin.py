from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Post, Contacts



class UserModel(UserAdmin):
    pass


admin.site.register(Post)
admin.site.register(Contacts)
# Register your models here.
