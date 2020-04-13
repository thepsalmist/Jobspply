from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework import filters


from jobs.models import Job
from .serializers import JobListSerializer, JobDetailSerializer
from .pagination import JobPageNumberPagination


class JobsListAPIView(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobListSerializer
    permission_classes = [
        IsAdminUser,
    ]
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "description"]
    pagination_class = JobPageNumberPagination


class JobsDetailAPIView(generics.RetrieveAPIView):
    queryset = Job.objects.all()
    serializer_class = JobDetailSerializer
    lookup_field = "slug"
    permission_classes = [
        IsAdminUser,
    ]
