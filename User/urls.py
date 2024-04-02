from django.urls import path
from .views import *

urlpatterns = [
    path('register/', Register.as_view()),
    path('login/', LoginView.as_view()),
    path('test/', UserListView.as_view()),
]