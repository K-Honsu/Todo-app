from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('update/<str:pk>/', views.updatePage, name='update'),
    path('delete/<str:pk>/', views.deleteTask, name='delete'),
    path('login/', views.loginPage, name='login-page'),
    path('logout/', views.logoutPage, name='logout-page'),
    path('register/', views.registerUser, name='register')
]
