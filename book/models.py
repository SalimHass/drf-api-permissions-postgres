from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField()
    author = models.CharField(max_length=255)
    rate=models.IntegerField()
    review = models.TextField()
    reviewer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    date_reviewed = models.DateTimeField(auto_now_add=True)
    review_updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title