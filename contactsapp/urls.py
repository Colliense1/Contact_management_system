from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_list, name='contact_list'),
    path('contact/<int:id>/', views.contact_detail, name='contact_detail'),
    path('contact/add/', views.contact_add, name='contact_add'),
    path('contact/<int:id>/edit/', views.contact_edit, name='contact_edit'),
    path('contact/<int:id>/delete/', views.contact_delete, name='contact_delete'),
    
]
