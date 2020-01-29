from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField
from PIL import Image
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    image= models.ImageField(default="default.jpg", upload_to="profile_pics")
    name = models.CharField(max_length=100, null=True)
    caption = models.TextField(max_length=250)
    likes = models.IntegerField(default=0, null=True)
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
    image_url = models.URLField(max_length=250, null=True)
    caption = models.TextField(max_length=250, null=True)
    post_date = models.DateTimeField(auto_now_add=True, null=True)

    @classmethod
    def show_pictures(cls):
        return cls.objects.order_by("post_date")[::1]

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Comments(models.Model):
    comment = models.TextField(max_length=100)
    picture = models.ForeignKey(Pictures, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
   

    
    def __str__(self):
        return self.comment
    def save_comment(self):
        self.save()
