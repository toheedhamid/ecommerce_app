from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name=" BlogHome"),
    path('about', views.about, name=" AboutUs"),
    path('contact', views.contact, name=" contactUs"),
    path('tracker', views.tracker, name=" TrackingStatus"),
    path('search', views.search, name=" search"),
    path('productview', views.productview, name=" productview"),
    path('checkout', views.checkout, name=" checkout")
]
