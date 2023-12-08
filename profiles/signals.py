from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile
import logging

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()



logger = logging.getLogger(__name__)

@receiver(post_save, sender=Profile)
def log_profile_creation(sender, instance, created, **kwargs):
    if created:
        logger.info(f"Profile created for user: {instance.user.username}")
