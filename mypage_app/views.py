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


User = get_user_model()

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


class UserUpdate(OnlyYouMixin,UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'mypage_app/user_form.html'

    def get_success_url(self):
        return resolve_url('mypage_app:user_detail', pk=self.kwargs['pk'])
