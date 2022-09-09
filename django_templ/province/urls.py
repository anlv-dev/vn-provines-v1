from django.urls import path
from . import views

app_name = 'province'
urlpatterns = [
    path('add_address/', views.address_create_view, name='add_address'), 
    path('<int:pk>/', views.address_edit_view, name='edit_address'), 
    path('ajax/districts/', views.getDistrictsByCity, name='ajax_districts'),
    path('ajax/wards/', views.getWardsByDistrict, name='ajax_wards'),
]