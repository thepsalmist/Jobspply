from rest_framework.serializers import ModelSerializer
from jobs.models import Job


class JobListSerializer(ModelSerializer):
    class Meta:
        model = Job
        fields = [
            "title",
            "slug",
            "description",
            "jobcategory",
            "job_url",
            "thumbnail",
            "publish",
        ]


class JobDetailSerializer(ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"
