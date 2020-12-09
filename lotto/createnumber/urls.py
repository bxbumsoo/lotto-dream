from django.urls import path, include
from . import views

urlpatterns = [
    path('createnumber/', views.createnumber),
    path('dream/', views.dream),
]
