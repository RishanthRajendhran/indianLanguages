from django.urls import path 
from . import views

app_name = "language"

urlpatterns = [
    path('create/', views.languageCreate, name="create"),
    path('<slug:slug>/', views.languageDetail, name="detail"),
]