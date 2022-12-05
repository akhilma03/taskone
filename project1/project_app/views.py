from django.shortcuts import render
from rest_framework import generics
from .serializer import productSerializer
from rest_framework.response import Response
from .models import Product

# Create your views here.
class productView(generics.ListAPIView):
    queryset= Product.objects.all()
    serializer_class=productSerializer
    
class productDetail(generics.RetrieveAPIView):
    queryset =Product.objects.filter() 
    serializer_class=productSerializer  
     
    

