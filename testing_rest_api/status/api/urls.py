from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('', views.StatusApiList.as_view(), name='list'),
    path('create/', views.StatusApiCreate.as_view(), name='create'),
    # path('detail/<id>/', views.StatusApiDetail.as_view(), name='detail'),
    # path('update/<id>/', views.StatusApiUpdate.as_view(), name='update'),
    # path('delete/<id>/', views.StatusApiDelete.as_view(), name='delete'),
]