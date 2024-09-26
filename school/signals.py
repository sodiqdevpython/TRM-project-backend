from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Organizations

@receiver(post_save, sender=Organizations)
def determine_is_city(sender, instance, created, **kwargs):
    if created:
        if instance.city:
            instance.is_city = True
        else:
            instance.is_city = False
        instance.save()