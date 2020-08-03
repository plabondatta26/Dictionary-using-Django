from django.db import models

# Create your models here.
class Dictionary(models.Model):
    word = models.CharField(max_length=100)
    definition = models.CharField(max_length=100)

    def __str__(self):
        return self.word + ' : '+ self.definition