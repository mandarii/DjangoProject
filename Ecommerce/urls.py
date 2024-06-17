from django.urls import path
from Ecommerce import views

urlpatterns = [
    path('index/',views.index, name='index'),
]