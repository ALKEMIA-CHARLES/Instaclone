from django.contrib import admin
from .models import Comments,Profile,DBUSER, Pictures
# Register your models here.


admin.site.register(Comments)
admin.site.register(Profile)
admin.site.register(DBUSER)
admin.site.register(Pictures)