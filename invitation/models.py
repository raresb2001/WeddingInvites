from django.db import models



# Create your models here.

class Invitation(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    venue = models.CharField(max_length=200)
    dress_code = models.CharField(max_length=100)
    img_upload = models.ImageField(upload_to='img/', null=True, blank=True)
    # file_upload = models.FileField(upload_to='files/', null=True)


    def __str__(self):
        return f"{self.title}"


