from django.db import models
from django.utils import timezone   
from django.contrib.auth.models import User     # one to many relationship

class Post(models.Model):
    title = models.CharField(max_length=100)
    content= models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)   # date_posted name wrong
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # if user deleted then delete their post also

    def __str__(self):
        return self.title
    