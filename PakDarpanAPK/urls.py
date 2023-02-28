from django.urls import path

# importing views from views.py
from . import views
from django.contrib.auth.views import LoginView
app_name = 'PakDarpanAPK'
urlpatterns = [
    path('', views.index, name='index'),
    path('login', LoginView.as_view(template_name='main/login.html'),name='login'),
]