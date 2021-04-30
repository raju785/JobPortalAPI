from django.shortcuts import render
from .models import JobOffer
from .serializers import JobSerializer
from rest_framework import generics

class JobList(generics.ListCreateAPIView):
    queryset = JobOffer.objects.all()
    serializer_class = JobSerializer

class JobListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobOffer.objects.all()
    serializer_class = JobSerializer
