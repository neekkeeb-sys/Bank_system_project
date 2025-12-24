# accountant/urls.py
from django.urls import path
from . import views

app_name = 'accountant'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('create-account/', views.create_account, name='create_account'),
    path('transaction/', views.transaction, name='transaction'),
]
