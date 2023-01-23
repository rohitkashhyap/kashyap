from django.urls import path
from ecom.views import *

app_name ='ecom'

urlpatterns = [
path('',HomeView.as_view(), name='home'),
path('create_new_category',CategoryCreateView.as_view(), name='categorycreate')
]
