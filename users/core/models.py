from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=500, blank=True)
    image= models.ImageField(upload_to='profiles/', blank=True)
    birthdate = models.DateField(blank=True, null=True)
    city= models.CharField(max_length=50, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()