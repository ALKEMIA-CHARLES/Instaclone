from django.shortcuts import render, redirect
from instagram.models import DBUSER, Comments, loggedinUser
# Create your views here.

def index(request):
    dbusers = DBUSER.show_db_users()
    return render(request, "main/index.html", context={"dbusers":dbusers})