from django.urls import path
from .views import *

urlpatterns = [
    path('', Home, name='home'),
    path('service/', Service, name='service'),
    path('contact/', Contact, name='contact'),
]