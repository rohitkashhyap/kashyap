from django.urls import path
from user.views import *

app_name='user'
urlpatterns = [
    # path('signup', signup, name='signup'),
    path('signup', SignupView.as_view(), name='signup'),
    # path('login', login_user, name='login'),
    path('login', SignInView.as_view(), name ='login'),
    path('logout', SignOutView.as_view(), name='logout')
]
