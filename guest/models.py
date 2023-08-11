from django.db import models

from invitation.models import Invitation


# Create your models here.

class Guest(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    is_attending = models.BooleanField(default=False)
    invitation = models.ForeignKey(Invitation, on_delete=models.CASCADE, null=True)
    profile = models.ImageField(upload_to="guest_profiles/", null=True, blank=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
