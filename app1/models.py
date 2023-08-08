from django.db import models

# Create your models here.

class New_message(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    text = models.TextField()

    def __str__(self) -> str:
        return self.name
