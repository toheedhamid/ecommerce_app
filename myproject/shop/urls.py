from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.index, name=" BlogHome"),
    path('about/', views.about, name=" AboutUs"),
    path('contact/', views.contact, name=" contactUs"),
    path('tracker/', views.tracker, name=" TrackingStatus"),
    path('search/', views.search, name=" search"),
    path('products/<int:myid>', views.productView, name=" productview"),
    path('checkout/', views.checkout, name=" checkout")
]
