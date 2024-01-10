from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index' ),
    path('input_data/', views.input_data, name='input_data'),
]
