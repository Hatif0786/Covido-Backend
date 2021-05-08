from django.db import models
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location='E:\journey\public\assets\images')

class News(models.Model):
   Created = models.DateTimeField(auto_now_add=True)
   Image = models.ImageField(upload_to="Uploads/IMAGES")
   Name = models.CharField(max_length=20)
   Suggestion = models.TextField(blank=True, default=" ")



   def __str__(self):
       return self.Name