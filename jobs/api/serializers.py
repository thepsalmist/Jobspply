from rest_framework.serializers import ModelSerializer
from jobs.models import Job


class JobsSerializer(ModelSerializer):
    class Meta:
        model = Job
        fields = [
            "title",
            "slug",
            "description",
            "category",
            "job_url",
            "thumbnail",
            "publish",
        ]

