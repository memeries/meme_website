from django.db import models


class Token(models.Model):
    secure_token = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.secure_token

