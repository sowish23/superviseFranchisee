from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# class Profile(models.Model):
#     objects = models.Manager()
#     user_id = models.OneToOneField(User, null=True, on_delete=models.CASCADE, verbose_name="USERID")
#     name = models.CharField(null=True, blank=True, max_length=10, verbose_name="NAME")

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user_id=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()

class UploadVideo(models.Model):
    user_id = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    video = models.FileField(upload_to='static/video/', null=True, verbose_name="video")

class UploadImgMenu(models.Model):
    user_id = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    menu_no = models.IntegerField(null=False, choices=((1,1), (2,2), (3,3), (4,4)),verbose_name="menu_number")
    image = models.ImageField(upload_to='static/image/', null=True, verbose_name="image")
