from django.urls import path
from mypage_app import views

# SET THE NAMESPACE!
app_name = 'mypage_app'


urlpatterns=[
        path('user_detail/<int:pk>/', views.UserDetail.as_view(), name='user_detail'),
        path('user_update/<int:pk>/', views.UserUpdate, name='user_update'),
        path('user_detail/<int:pk>/follow/', views.follow, name='follow'),

]
