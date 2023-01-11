from .views import createuser, login, logout
from django.urls import re_path

urlpatterns = [
    re_path(r'createuser', createuser.as_view(), name='createuser'),
    re_path(r'login', login.as_view(), name='login'),
    re_path(r'logout', logout.as_view(), name='logout')
]