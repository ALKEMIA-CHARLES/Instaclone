from django.shortcuts import render, redirect
from instagram.models import DBUSER, Comments, Profile
from django.http import HttpResponseRedirect
from django.urls import reverse
from instagram.forms import Uploadform, Signupform, LoggedinUserform
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    posts = DBUSER.objects.all()[::-1]
    current_user = request.user
    comments = Comments.objects.all()
    try:
        current_profile = request.user
    except loggedinUser.DoesNotExist:
        current_profile = None

    if request.method == "POST":
        form = Uploadform(request.POST)

        if form.is_valid():
            post = form.save(commit=False)

            post.profile = current_user
            post.user_profile = current_profile

            post.save()
            form = Uploadform()
            return HttpResponseRedirect(reverse("index"))

    else:
        form = Uploadform()
    return render(request, "main/index.html", context={
                                                        "posts":posts,
                                                       "Uploadform":Uploadform})


def search(request):
    if request.method == "GET":
        search_term = request.GET.get("search")
        searched_db_users = DBUSER.search_dbuser_by_name(search_term)
        results = len(searched_db_users)
        message = "{}".format(search_term)
        
        return render(request, "main/search.html", context={"message":message,
                                                            "dbusers":searched_db_users,
                                                            "results":results})
    else:
        message = "You have not searched for any user"
        return render(request, "main/index.html", context={"message":message})


def register(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid ():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account has been created! You are now able to login')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, "auth/signup.html", context={'form': form})

@login_required
def profile(request):
    return render(request, "main/profile.html")

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("user_login"))

