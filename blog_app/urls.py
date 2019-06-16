from django.conf.urls import url
from django.urls import path
from blog_app import views

app_name = 'blog_app'

urlpatterns = [

    path('',views.SchoolListView.as_view(),name='list'),
    url(r'^(?P<pk>\d+)/',views.SchoolDetailView.as_view(),name='detail'),
    path('create/',views.SchoolCreateView.as_view(),name='create'),
    url(r'^update/(?P<pk>\d+)/',views.SchoolUpdateView.as_view(),name='update'),
    url(r'^delete/(?P<pk>\d+)/',views.SchoolDeleteView.as_view(),name='delete'),
]
