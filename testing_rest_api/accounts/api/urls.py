from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from .import views

urlpatterns = [
    path('', views.AuthView.as_view()),
    path('refresh/', refresh_jwt_token),
    path('register/', views.RegisterView.as_view()),
]