from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_delete, post_save, pre_delete
from django.dispatch import receiver 
# Create your models here.

def custom_upload_to(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profile/'+ filename

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)

    class Meta:
        ordering = ['user__username']

@receiver(post_delete, sender=Profile)
def Profile_delete(sender, instance, **kwargs):
    """ Borra los ficheros de las fotos que se eliminan. """
    print("post-delete"+"-"*60)
    print(instance.avatar)
    instance.avatar.delete(False)

@receiver(pre_delete, sender=Profile)
def profile_pre_delete(sender, instance, **kwargs):
    """ Borra los ficheros de las fotos que se eliminan. """
    print("pre-delete"+"-"*60)
    print(instance.avatar)
    instance.avatar.delete(False)

@receiver(post_save, sender=User)    
def ensure_profile_exists(sender, instance, **kwargs):
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=instance)
        #print('Se acaba de crear un usuario y su perfil enlazado')