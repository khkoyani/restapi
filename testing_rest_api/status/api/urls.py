from django.contrib import admin
from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token



urlpatterns = [
    path('', views.StatusApiList.as_view(), name='list'),
    path('<int:id>/', views.StatusApiDetail.as_view(), name='detail'),

]