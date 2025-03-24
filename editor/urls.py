from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('run-code/', views.run_code, name='run_code'),
    path('save-code/', views.save_code, name='save_code'),
    path('shared-code/', views.shared_code, name='shared_code'),
    path('process-sidebar/', views.process_sidebar, name='process_sidebar'),
    path('user/', views.user, name='user'),
    path('get-saved-codes/', views.get_saved_codes, name='get_saved_codes'),
    path('get-shared-codes/', views.get_shared_codes, name='get_shared_codes'),
    path('delete-code/', views.delete_code, name='delete_code'),
    path('delete-code-shared/', views.delete_code_shared, name='delete_code_shared'),
    path('search/', views.search_view, name='search'),
]
