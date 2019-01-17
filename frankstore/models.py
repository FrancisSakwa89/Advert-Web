from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class Advert(models.Model):
  name = models.CharField(max_length=60,default='name')
  image = models.ImageField(upload_to = 'photos/')
  category = models.CharField(max_length=60)
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

def __str__(self):
        return f'{self.user.username} Profile'

@property
def image(self):
    if self.photo and hasattr(self.photo, 'url'):
        return self.photo.url

# @classmethod
# def search_by_username(cls,search_term):
#     search_result = cls.objects.filter(user__username__icontains=search_term)
#     return search_result
def save_profile(self):
    self.save()


class Category(models.Model):
  category = models.CharField(max_length=60)

  def __str__(self):
    return self.category
  class Meta:
    ordering = ['category']

  def save_category(self):
    self.save()

  def delete_category(self):
    self.delete()

  @classmethod
  def update_category(cls,id,category):
    category = cls.objects.get(pk=id)
    category = cls(category=category)
    category.save()

