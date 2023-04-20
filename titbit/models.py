from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Post(models.Model):
    """
    Create Post Model with time
    Like/Unlike
    """
    user = models.ForeignKey(
        User, related_name='posts',
        on_delete=models.CASCADE)
    body = models.CharField(max_length=250)
    # Time
    created_at = models.DateTimeField(auto_now_add=True)
    # Likes
    likes = models.ManyToManyField(User, related_name='post_like', blank=True)
    # Count the likes
    def number_of_likes(self):
        return self.likes.count()

    def __str__(self):
        return (
            f'{self.user} '
            f'({self.created_at:%d-%m-%Y %H:%M}): '
            f'{self.body}'
        )


class Profile(models.Model):
    """
    Create a User Profile Model
    List follows and followed by
    Insert date to last update
    Insert profile picture
    """
    user = models.OneToOneField(User,
                                related_name="profile",
                                on_delete=models.CASCADE)
    follows = models.ManyToManyField('self',
                                    related_name='followed_by',
                                    symmetrical=False,
                                    blank=True)

    date_modified = models.DateTimeField(User, auto_now=True)
    # Profile picture
    profile_picture = models.ImageField(null=True, blank=True,
                                        upload_to="images/")

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    Create Profile when new User signs up
    """
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        # Have the user follow themselves
        user_profile.follows.set([instance.profile.id])
        user_profile.save()
