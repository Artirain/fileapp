from django.db import models

# Create your models here.
class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    description = models.TextField()

    def __str__(self):
        return self.description
    
    