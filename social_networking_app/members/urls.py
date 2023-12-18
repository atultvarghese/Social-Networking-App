from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('home', views.home, name='home'),
]

urlpatterns += [
    path("accounts/", include("django.contrib.auth.urls")),
]