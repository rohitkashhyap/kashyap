from django.urls import path
from home.views import *

app_name = 'home'
urlpatterns = [
    path('',home, name='home'),
    path('contact', ContactView.as_view(), name='contact'),
    path('aboutus', about, name='about')
]