from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('band_list/', views.band_list, name='band_list'),
    path('<int:pk>/', views.band_detail, name='band_detail'),
]

"""
URL configuration for the 'theband' application.

This module defines the URL patterns for the views in the 'theband'
application, mapping URL paths to their corresponding view functions.

The following routes are defined:
- '' : The home page, handled by the `home` view.
- 'band_list/' : The page displaying a list of all bands, handled by the `band_list` view.
- '<int:pk>/' : The detail page for a specific band identified by its primary key (pk), 
  handled by the `band_detail` view.
"""
