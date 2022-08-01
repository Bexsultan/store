from django.urls import path
from app.views import ProductList, ProductDetail

urlpatterns = [
    path('<int:pk>/', ProductDetail.as_view()),
    path('', ProductList.as_view())
]
