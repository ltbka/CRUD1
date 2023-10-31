from django.urls import path
from . import views

urlpatterns = [
    path('', views.CategoryCreateListView.as_view())
]
