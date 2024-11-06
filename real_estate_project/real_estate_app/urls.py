from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),   # Login page URL
    path('signup/', views.signup_view, name='signup'),  # Signup page URL
    path('', views.home, name='home'),                  # Home page URL
]
