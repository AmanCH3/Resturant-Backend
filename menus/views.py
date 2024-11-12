from rest_framework import generics
from .models import Menu
from menus.serializers import MenuSerializer

class MenuListCreate(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer