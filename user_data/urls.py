from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('verify-email/', views.VerifyEmailView.as_view(), name='verify_email'),
    path('user-status/', views.UserStatusView.as_view(), name='user_status'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
]
