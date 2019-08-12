from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.shortcuts import redirect, resolve_url
from django.views import generic
from .forms import UserUpdateForm
# from login_app import models
from django.views.generic import (DetailView,
                                    UpdateView)
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import get_user_model
from login_app.models import UserProfileInfo,Relationship
from django.urls import reverse_lazy


User = get_user_model()
profile = UserProfileInfo

@method_decorator(login_required, name='dispatch')
class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        user = self.request.user
        return user.pk == self.kwargs['pk'] or user.is_superuser

@method_decorator(login_required, name='dispatch')
class UserDetail(DetailView):
    context_object_name = 'user_detail'
    model = User
    template_name = 'mypage_app/user_detail.html'


# @method_decorator(login_required, name='dispatch')
# class UserProfileInfoDetail(DetailView):
#     context_object_name = 'profileInfo_detail'
#     model = UserProfileInfo
#     template_name = 'mypage_app/user_detail.html'
#
#

@login_required
class UserUpdate(OnlyYouMixin,UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'mypage_app/user_form.html'

    def get_success_url(self):
        return resolve_url('mypage_app:user_detail', pk=self.kwargs['pk'])



@login_required
def follow(request, *args, **kwargs):
    followed_user = User.objects.get(id=kwargs['pk'])
    follow_user = request.user
    follow = Relationship.objects.filter(follow=followed_user).filter(follower=follow_user).count()
    if follow_user.follow_num == None:
        follow_user.follow_num == 0
    if followed_user.follower_num == None:
        followed_user.follower_num == 0


    # unfollow
    if follow > 0:
        following = Relationship.objects.get(follow=followed_user, follower=follow_user)
        following.delete()
        follow_user.follow_num -= 1
        followed_user.follower_num -= 1
        follow_user.save()
        followed_user.save()
        return redirect(reverse_lazy('mypage_app:user_detail', kwargs={'pk': kwargs['pk']}))


#follow
    follow_user.follow_num += 1
    followed_user.follower_num += 1
    follow_user.save()
    followed_user.save()
    relationship = Relationship()
    relationship.follower = follow_user
    relationship.follow = followed_user
    relationship.save()
    return redirect(reverse_lazy('mypage_app:user_detail', kwargs={'pk': kwargs['pk']}))
