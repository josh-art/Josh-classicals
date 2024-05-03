from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('login/', views.login, name="login"),
    path('handlesignup/', views.handlesignup, name="handlesignup"),
    path('handlelogin/', views.handlelogin, name="handlelogin"),
    path('signup/', views.signup, name="signup"),
]
