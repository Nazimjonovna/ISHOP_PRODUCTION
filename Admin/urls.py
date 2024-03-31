from django.urls import path
from .views import *

urlpatterns = [
    path('register/', AdminRegister.as_view()),
    path('login/', LoginView.as_view()),
    path('test/', SS.as_view()),
]