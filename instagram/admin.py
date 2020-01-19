from django.contrib import admin
from .models import Comments,loggedinUser,DBUSER
# Register your models here.


admin.site.register(Comments)
admin.site.register(loggedinUser)
admin.site.register(DBUSER)