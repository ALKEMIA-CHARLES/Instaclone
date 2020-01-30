from django.contrib import admin
from .models import Pictures, Post, Profile, Comments
# Register your models here.


admin.site.register(Pictures)
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Comments)