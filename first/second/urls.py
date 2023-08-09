from django.urls import path
from .views import index, about, phone_number,leave

urlpatterns = [
    path('', index),
    path('about', about),
    path('phone_number', phone_number),
    path("leave", leave),
]
