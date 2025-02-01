from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('run-code/', views.run_code, name='run_code'),
    path('process-sidebar/', views.process_sidebar, name='process_sidebar'),
]