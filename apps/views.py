from drf_spectacular.utils import extend_schema
from rest_framework import generics
from apps.models import Brand, Product
from apps.serializers import BrandCreateSerializer


@extend_schema(
    tags=['Brands']
)
class ProductBrandListAPIView(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandCreateSerializer


@extend_schema(
    tags=['Brands']
)
class ProductBrandDetailAPIView(generics.RetrieveAPIView):
    serializer_class = BrandCreateSerializer

    def get_queryset(self):
        product_id = self.kwargs['product_id']
        return Brand.objects.filter(product__id=product_id)
