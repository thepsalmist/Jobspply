from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(
        default="./media/Author.jpg", blank=True, null=True, upload_to="Profiles"
    )
    bio = models.TextField(blank=True, null=True)
    work_title = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    work = models.TextField(blank=True, null=True)
    education = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} Profile"


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return f"{self.message} from {self.name}"
