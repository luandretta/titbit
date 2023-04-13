from django.db import models
from django.contrib.auth.models import User


"""
Create a User Profile Model
"""
class Profile(models.Model):
    user = models.OneToOneField(User,
        related_name="profile", on_delete=models.CASCADE)
    follows = models.ManyToManyField('self',
        related_name='followed_by',
        symmetrical=False,
        blank=True)

    def __str__(self):
        return self.user.username
