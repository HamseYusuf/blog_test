from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField( max_length=50)
    content = models.TextField()
    data_poste = models.DateTimeField( auto_now=True,)
    author = models.ForeignKey(User,  on_delete=models.CASCADE)

    def __str__(self):
        return self.content
    