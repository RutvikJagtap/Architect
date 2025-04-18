from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home, name="Home"),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('contact/', views.contact, name='contact'),
]
