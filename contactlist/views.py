from django.shortcuts import render
from rest_framework import generics
from .models import Contact
from .serializers import ContactSerializer

# Create your views here.
class Contactlist(generics.ListCreateAPIView):

    queryset = Contact.objects.all()
    serializer_class = ContactSerializer