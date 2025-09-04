"""
Sample app URLs
"""
from django.urls import path
from . import views

app_name = 'sample'

urlpatterns = [
    path('people/', views.person_list, name='person_list'),
    path('people/<int:pk>/', views.person_detail, name='person_detail'),
    path('people/create/', views.person_create, name='person_create'),
    path('people/<int:pk>/edit/', views.person_update, name='person_update'),
    path('people/<int:pk>/delete/', views.person_delete, name='person_delete'),
]
