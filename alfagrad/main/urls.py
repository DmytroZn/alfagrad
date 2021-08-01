from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path('view/<str:pk>/', views.view, name='view'),
    path('about-us/', views.about_us, name='about_us'),
    path('all-projects/', views.all_projects, name='all_projects'),
    path('robots.txt/', views.robots_txt, name='robots_txt'),
    

]
