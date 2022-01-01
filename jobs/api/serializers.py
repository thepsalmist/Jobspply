from rest_framework import serializers
from jobs.models import Job


class JobListSerializer(serializers.ModelSerializer):
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


class JobDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"
