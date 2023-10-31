from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Category
from .serializers import CategorySerializer

class CategoryCreateListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = ...
    # permission_classes = (permissions.IsAdminUser,)
    
    def get_permissions(self):
        if self.request.method == 'POST':
            return permissions.IsAdminUser(),
        return permissions.AllowAny(),
    
