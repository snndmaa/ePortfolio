from django.db import models


class Contact(models.Model):
    name    = models.CharField(max_length=50)
    email   = models.EmailField(max_length=70)
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self) -> str:
        return self.subject