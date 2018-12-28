from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('amadon/', views.index),
    path('amadon/additem/<int:id>/', views.addProduct),
    path('amadon/cart/', views.cart),
    path('amadon/cart/update/<int:id>', views.updateProduct),
    path('amadon/cart/purchase/', views.checkout),
]