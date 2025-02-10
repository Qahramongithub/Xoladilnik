from django.urls import path
from apps.views import ProductBrandListAPIView, ProductBrandDetailAPIView

urlpatterns = [
    path('products/brands/list', ProductBrandListAPIView.as_view(), name='product-brand-list'),
    path('products/<int:product_id>/brands/<int:pk>/', ProductBrandDetailAPIView.as_view(), name='product-brand-detail'),
]
