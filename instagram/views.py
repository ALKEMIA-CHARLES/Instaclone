from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from instagram.models import Post,Pictures,Comments, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import Uploadindexphotoform, UserUpdateForm

# Create your views here.

class DbListView(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'main/index.html'
    context_object_name = 'posts'
    ordering = ['-post_date']

class DbDetailView(LoginRequiredMixin,DetailView):
    model = Post
    template_name = 'main/detail.html'

class DbCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'main/dbuser_form.html'
    fields = ['image', 'caption']

    def form_valid(self, form):
        form.instance.masterkey = self.request.user
        return super().form_valid(form)

class DbUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'main/dbuser_form.html'
    fields = ['image', 'caption']
    
    def form_valid(self, form):
        form.instance.masterkey = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.masterkey:
            return True
        return False

class DbDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'main/post_confirm_delete.html'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.masterkey:
            return True
        return False

def search(request):
    if request.method == "GET":
        search_term = request.GET.get("search")
        searched_post = Post.search_post_by_name(search_term)
        results = len(searched_post)
        message = "{}".format(search_term)
        
        return render(request, "main/search.html", context={"message":message,
                                                            "posts":searched_post,
                                                            "results":results})
    else:
        message = "You have not searched for any user"
        return render(request, "main/index.html", context={"message":message})


def register(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account has been created! You are now able to login')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, "auth/signup.html", context={'form': form})

@login_required
def profile(request):
    pics = Pictures.objects.all()[::1]
    if request.method == "POST":
        form = Uploadindexphotoform(request.POST,request.FILES, instance=request.user.profile)

        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = Uploadindexphotoform(instance=request.user.profile)
    return render(request, "main/profile.html", context={"form":form,
                                                         "pics":pics,
                                                      })
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("user_login"))

