from rest_framework import serializers
from .models import JobOffer

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobOffer
        fields = "__all__"