from django.conf.urls import url
from django.urls import path
from blog_app import views

app_name = 'blog_app'

urlpatterns = [

    path('',views.PostListView.as_view(),name='list'),
    url(r'^(?P<pk>\d+)/',views.PostDetailView.as_view(),name='detail'),
    path('create/',views.PostCreateView.as_view(),name='create'),
    url(r'^update/(?P<pk>\d+)/',views.PostUpdateView.as_view(),name='update'),
    url(r'^delete/(?P<pk>\d+)/',views.PostDeleteView.as_view(),name='delete'),
]
