from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('update/<str:pk>/', views.updatePage, name='update'),
    path('delete/<str:pk>/', views.deleteTask, name='delete'),
]
