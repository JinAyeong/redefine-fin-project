from django.urls import path
from . import views

urlpatterns = [
    # path('', views.api_test),
    path('save_rate/', views.save_rate),
    path('', views.index, name='index'),
]
