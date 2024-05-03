from django.urls import path
from . import views

app_name = 'shops'

urlpatterns = [
    path('', views.product_list, name='Home'),
    path('contact/', views.contact, name='Contact'),
    path('reach/', views.feedback, name='reach'),
    path('PortFolio/', views.folio, name='folio'),
    path('About/', views.about, name='about'),
    path('addfeatured/', views.AddFeatured, name='AddFeatured'),

]
