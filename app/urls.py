from django.urls import path
from app.views import ProductList, ProductDetail, ReviewCreateView, UserProductView

urlpatterns = [
    path('<int:pk>/', ProductDetail.as_view()),
    path('', ProductList.as_view()),
    path("review/", ReviewCreateView.as_view()),
    path('user-product', UserProductView.as_view())

]
