from django.urls import path, include
from .views import JobList, JobListDetail

urlpatterns = [
    path('jobslist', JobList.as_view(), name='joblist'),
    path('jobdetails/<int:pk>/', JobListDetail.as_view(), name='jobdetails'),
]
