from django.urls import path
from . import views

app_name = 'shops'

urlpatterns = [
    path('', views.product_list, name='Home'),
    path('contact me/', views.contact, name='Contact'),
    path('reach me/', views.feedback, name='reach'),

]
