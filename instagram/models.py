from django.db import models
from pyuploadcare.dj.models import ImageField
# Create your models here.

class DBUSER(models.Model):
    name= models.CharField(max_length=100)
    image = models.ImageField()
    db_comment = models.CharField(max_length=100)
    likes = models.IntegerField(default=0)
    post_date = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField(max_length=250)

    def __str__(self):
        return self.name
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
  
class loggedinUser(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/') 
    caption = models.TextField(blank=True)
    Bio = models.TextField(max_length=700)
    dbuser =  models.ForeignKey(DBUSER, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name, self.image
    def save_loggedin_user(self):
        return self.save()
    def delete_post(self):
        self.delete()
    def update_caption(self, new_cap):
        self.caption = new_cap
        self.save()
  

class Comments(models.Model):
    comment = models.TextField(max_length=100)
    loggedin_user_comment = models.ForeignKey(loggedinUser, on_delete=models.CASCADE)


    
    def __str__(self):
        return self.comment
    def save_comment(self):
        self.save()
