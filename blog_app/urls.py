from django.conf.urls import url
from django.urls import path
from blog_app import views

app_name = 'blog_app'

urlpatterns = [

    path('',views.PostListView.as_view(),name='list'),
    path('post/<int:pk>/',views.PostDetailView.as_view(),name='detail'),
    path('create/',views.PostCreateView.as_view(),name='create'),
    path('update/<int:pk>/',views.PostUpdateView.as_view(),name='update'),
    path('delete/<int:pk>/',views.PostDeleteView.as_view(),name='delete'),
    path('post/<int:pk>/comment/', views.CommentCreateView.as_view(), name='add_comment_to_post'),
    path('post/<int:pk>/like/', views.like, name='like'),
]
