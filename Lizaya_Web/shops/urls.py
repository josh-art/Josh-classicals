from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'shops'

urlpatterns = [
    path('', views.product_list, name='Home'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
    path('contact me/', views.contact, name='Contact'),
    path('reach me/', views.feedback, name='reach'),
    url(r'^add user/$', views.addUser, name='AddUser'),
    path('addfeatured/', views.AddFeatured, name='AddFeatured'),

]
