from django.conf.urls import url
from .views import DbListView, DbDetailView
from . import views

urlpatterns = [
    url(r'^$', DbListView.as_view(), name='index'),
    url(r'^post/(?P<pk>\d+)/$', DbDetailView.as_view(), name='post-detail'),
    url(r'^search/$', views.search, name="search"),
]