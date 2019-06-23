from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.shortcuts import redirect, resolve_url
from django.views import generic
from .forms import UserUpdateForm
from login_app.models import User, UserProfileInfo
from django.views.generic import (DetailView,
                                    UpdateView)





class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        user = self.request.user
        return user.pk == self.kwargs['pk'] or user.is_superuser


class UserDetail(OnlyYouMixin, DetailView):
    context_object_name = 'user_detail'
    model = User
    template_name = 'mypage_app/user_detail.html'


class UserUpdate(OnlyYouMixin,UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'mypage_app/user_form.html'

    def get_success_url(self):
        return resolve_url('mypage_app:user_detail', pk=self.kwargs['pk'])
