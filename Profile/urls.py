from django.urls import path
from . import views
app_name = "Profile"
urlpatterns = [
    path('register', views.RegisterView, name='register'),
    path('edit/<int:pk>', views.RegisterView, name="edit"),
    path('dashboard', views.Dashboard, name="dashboard"),
    path('login', views.LoginView, name="login"),
    path('logout', views.LogoutView, name="logout"),
]
