
from django.urls import path

from django.contrib import admin
from django.urls import path, include
from prod import views

urlpatterns = [
    path('prod/', views.ProductListView.as_view(), name="prod_cre_list"),
    path('prod/<int:pk>', views.ProductDetailsView.as_view(), name="prod_up_del"),
    ]