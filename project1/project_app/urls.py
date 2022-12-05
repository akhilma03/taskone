from django.urls import path
from . import views
from .views import *

urlpatterns = [
    
    path('',productView.as_view(),name='products'),
    path('productdetail/<int:pk>/',productDetail.as_view(),name='productdetail')
    
   
    

]
