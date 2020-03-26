from rest_framework import generics

from jobs.models import Job
from .serializers import JobsSerializer


class JobsListAPIView(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobsSerializer
