from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField
from PIL import Image
from django.urls import reverse

from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    print("=========================================[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]=")

    if created:
        Profile.objects.create(user=instance)
        print("==========================================")


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'



class Post(models.Model):
    image= models.ImageField(default="default.jpg", upload_to="profile_pics")
    name = models.CharField(max_length=100)
    caption = models.TextField(max_length=250)
    likes = models.IntegerField(default=0,)
    post_date = models.DateTimeField(auto_now_add=True)
    masterkey = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})
    @classmethod
    def show_posts(cls):
        return cls.objects.order_by("post_date")[::1]
    @classmethod
    def search_post_by_name(cls,search):
        return cls.objects.filter(name__icontains=search)


class Pictures(models.Model):
    image_url = models.URLField(max_length=250)
    caption = models.TextField(max_length=250)
    post_date = models.DateTimeField(auto_now_add=True )


class Comments(models.Model):
    comment = models.CharField(max_length=200)
    post =  models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

    
    def __str__(self):
        return self.comment
    def save_comment(self):
        self.save()