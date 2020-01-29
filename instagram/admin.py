from django.contrib import admin
from .models import Comments, Pictures,Post, Profile
# Register your models here.


admin.site.register(Comments)
admin.site.register(Post)
admin.site.register(Pictures)
admin.site.register(Profile)