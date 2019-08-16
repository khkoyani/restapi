from django.urls import path
from . import views

urlpatterns = [
    path('', views.UpdateJsonListView.as_view(), name='list'),
    path('<int:id>/', views.UpdateJsonDetailView.as_view(), name='detail'),
]