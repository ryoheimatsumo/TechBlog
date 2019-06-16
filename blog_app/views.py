from django.shortcuts import render
from django.views.generic import (View,TemplateView,
                                    ListView,DetailView,
                                    CreateView,UpdateView,DeleteView)
from django.urls import reverse_lazy
from . import models
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User



# Create your views here.
@method_decorator(login_required, name='dispatch')
class PostListView(ListView):
    context_object_name = 'posts'
    model = models.Post
    # school_list

@method_decorator(login_required, name='dispatch')
class PostDetailView(DetailView):
    context_object_name = 'post_detail'
    model = models.Post
    template_name = 'blog_app/post_detail.html'

@method_decorator(login_required, name='dispatch')
class PostCreateView(CreateView):
    fields = ('title','text')
    model = models.Post
    success_url = reverse_lazy("blog_app:list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostCreateView, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class PostUpdateView(UpdateView):
    fields = ('title','text')
    model = models.Post

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostUpdateView, self).form_valid(form)



@method_decorator(login_required, name='dispatch')
class PostDeleteView(DeleteView):
    model=models.Post
    success_url = reverse_lazy("blog_app:list")

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)
