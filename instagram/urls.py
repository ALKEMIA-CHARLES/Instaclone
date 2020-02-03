from django.conf.urls import url
from .views import DbListView, DbDetailView, DbCreateView,DbUpdateView, DbDeleteView
from . import views

urlpatterns = [
    url(r'^$', DbListView.as_view(), name='index'),
    url(r'^post/(?P<pk>\d+)/$', DbDetailView.as_view(), name='post-detail'),
    url(r'^post/new/$', DbCreateView.as_view(), name='post-create'),
    url(r'^post/(?P<pk>\d+)/update/$', DbUpdateView.as_view(), name='post-update'),
    url(r'^post/(?P<pk>\d+)/delete/$', DbDeleteView.as_view(), name='post-delete'),
    url(r'^comments/(\d+)/$', views.post_comments , name='post-comment'),
    url(r'^search/$', views.search, name="search"),
]