from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework import filters


from jobs.models import Job
from .serializers import JobListSerializer, JobDetailSerializer
from .pagination import JobPageNumberPagination


class JobsListSearchAPIView(generics.ListAPIView):
    serializer_class = JobListSerializer
    permission_classes = [
        IsAdminUser,
    ]
    queryset = Job.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "description"]
    pagination_class = JobPageNumberPagination


class JobsListAPIView(generics.ListAPIView):
    serializer_class = JobListSerializer
    permission_classes = [
        IsAdminUser,
    ]
    queryset = Job.objects.all()


class JobsDetailAPIView(generics.RetrieveAPIView):
    queryset = Job.objects.all()
    serializer_class = JobDetailSerializer
    lookup_field = "slug"
    permission_classes = [
        IsAdminUser,
    ]
