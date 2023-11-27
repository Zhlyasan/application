from django.urls import path
from .views import index
from .views import *

urlpatterns = [
    path('', index),
]
