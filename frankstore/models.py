from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class Advert(models.Model):
  name = models.CharField(max_length=60,default='name')
  image = models.ImageField(upload_to = 'photos/')
  location = models.CharField(max_length=60)
  prize = models.CharField(max_length=60,default='kshs.')
  email = models.EmailField(max_length=60,default='email')
  description = models.TextField(default='description')
  pub_date = models.DateTimeField(auto_now_add=True)

class Profile(models.Model):
  photo = models.ImageField(upload_to = 'photos/')
  bio = models.CharField(max_length=200)
  contact = models.EmailField()
  advert = models.ForeignKey(Advert, on_delete=models.CASCADE,blank=True,null=True)
  user = models.OneToOneField(User, on_delete=models.CASCADE)

  @receiver(post_save, sender=User)
  def create_user_profile(sender, instance, created, **kwargs):
    if created:
      Profile.objects.create(user=instance)

  @receiver(post_save, sender=User)
  def save_user_profile(sender, instance, **kwargs):
      instance.profile.save()

  post_save.connect(save_user_profile, sender=User)

  def save_profile(self):
    self.save()

  def delete_profile(self):
    self.delete()

