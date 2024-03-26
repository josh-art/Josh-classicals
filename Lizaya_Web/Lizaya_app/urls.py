from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import PostCreateView



urlpatterns = [
    path('', views.error, name='error'),
    path('home', views.index1, name='index'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post_update', views.post_update, name='post_update'),
    path('feedback/', views.contactForm, name='feedback'),
    path('Contact_Us/', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('gallery', views.profile_posts, name='gallery'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
