from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('api/form_submission/', views.form_submission, name='form_submission'),
]