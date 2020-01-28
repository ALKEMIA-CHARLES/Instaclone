from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField
from PIL import Image
from django.urls import reverse
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    age = models.IntegerField(default=0)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics') 
    caption = models.TextField(blank=True)
    bio = models.TextField(max_length=700)


    def __str__(self):
        return f'{self.user.username} Profile'
    def save(self):
        super().save()
    
        img  = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
    def delete_post(self):
        self.delete()
    def update_caption(self, new_cap):
        self.caption = new_cap
        self.save()
  
class DBUSER(models.Model):
    name= models.CharField(max_length=100)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    db_comment = models.CharField(max_length=100)
    likes = models.IntegerField(default=0)
    post_date = models.DateTimeField(auto_now_add=True)
    caption = models.TextField(max_length=500, null=True)
    image_url = models.URLField(max_length=250)
    profile = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})
    def save_db_user(self):
        return self.save()
    def get_remote_image(self):
        if self.image_url and not self.image:
            result = request.urlretrieve(self.image_url)
        self.image.save(
                os.path.basename(self.image_url),
                File(open(result[0], 'rb'))
                )
        self.save()
   
    @classmethod
    def show_db_users(cls):
        return cls.objects.order_by("post_date")[::1]
    @classmethod
    def search_dbuser_by_name(cls,search):
        return cls.objects.filter(name__icontains=search)
class Comments(models.Model):
    comment = models.TextField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    db_user = models.ForeignKey(DBUSER, on_delete=models.CASCADE, null=True)

    
    def __str__(self):
        return self.comment
    def save_comment(self):
        self.save()
