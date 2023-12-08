from django.urls import path
from .views import home, register, profile
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('accounts/profile/', profile, name='profile'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]
