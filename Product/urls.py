from django.urls import path
from .views import *

urlpatterns = [
    path('parametr/', ParametrView.as_view()),
    path('parametr/<int:id>/', EditParametrView.as_view()),
    path('category/', CategoryView.as_view()),
    path('category/<int:id>/', EditCategoryView.as_view()),
    path('news/', NewsView.as_view()),
    path('news/<int:id>/', EditNewsView.as_view()),
    path('brand/', BrandView.as_view()),
    path('brand/<int:id>/', EditBrandView.as_view()),
    path('contact/', ContactView.as_view()),
    path('contact/<int:id>/', EditContactView.as_view()),
    path('offer/', PublicOfferView.as_view()),
    path('offer/<int:id>/', EditPublicOfferView.as_view()),
]