from django.db import models
from django.utils import timezone

class Comment(models.Model):
     Name = models.CharField(max_length=128)
     url = models.CharField(max_length=255)
     Email = models.CharField(max_length=255)
     Body = models.TextField()
     dt = models.DateTimeField()

     def was_published_recently(self):
         return self.pub_date >= (timezone.now() - datetime.timedelta(days = 3))
