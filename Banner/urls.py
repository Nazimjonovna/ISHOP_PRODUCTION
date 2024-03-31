from django.urls import path
from .views import *

urlpatterns = [
    path('', BannerView.as_view()),
    path('<int:id>/', EditBannerView.as_view())
]