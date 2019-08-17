from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('', views.StatusApiList.as_view(), name='list'),
    # path('create/', views.StatusApiCreate.as_view(), name='create'),
    # path('<int:id>/', views.StatusApiDetail.as_view(), name='detail'),
    # path('<id>/update/', views.StatusApiUpdate.as_view(), name='update'),
    # path('<id>/delete/', views.StatusApiDelete.as_view(), name='delete'),
]