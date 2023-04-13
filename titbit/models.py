from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


"""
Create a User Profile Model
"""
class Profile(models.Model):
    user = models.OneToOneField(User,
                                related_name="profile", 
                                on_delete=models.CASCADE)
    follows = models.ManyToManyField('self',
                                    related_name='followed_by',
                                    symmetrical=False,
                                    blank=True)

    date_modified = models.DateTimeField(User, auto_now=True)

    def __str__(self):
        return self.user.username

"""
Create Profile when new User signs up
"""
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        # Have the user follow themselves
        user_profile.follows.set([instance.profile.id])
        user_profile.save()

