from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response

from .models import *
from .serializers import *
from rest_framework import generics


class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    

    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        product_name = request.data.get('name')
        
        if Product.objects.filter(name=product_name).exists():
            return Response({"error": "Product with the same name already exists."}, status=status.HTTP_404_NOT_FOUND)

        return super().create(request, *args, **kwargs)
    



class ProductDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        product_name = request.data.get('name')
        
        # Check if there's another product with the same name and it's not the same instance
        if Product.objects.filter(name=product_name).exclude(pk=instance.pk).exists():
            return Response({"error": "Product with the same name already exists."}, status=status.HTTP_404_NOT_FOUND)

        return super().update(request, *args, **kwargs)

