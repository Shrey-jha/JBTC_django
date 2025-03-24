from django.urls import path
from . import views
from .views import feedback_view, feedback_thanks_view

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('load_form/', views.load_form, name='load_form'),
    path('feedback/', feedback_view, name='feedback'),  # Added name here
    path('thanks/', feedback_thanks_view, name='feedback_thanks'),
]
