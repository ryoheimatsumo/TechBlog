from django.shortcuts import render, get_object_or_404
from django.views.generic import (View,TemplateView,
                                    ListView,DetailView,
                                    CreateView,UpdateView,DeleteView)
from django.urls import reverse_lazy
from . import models
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.shortcuts import redirect



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


@method_decorator(login_required, name='dispatch')
class CommentCreateView(CreateView):
    fields = ('text',)
    model = models.Comment
    success_url = reverse_lazy("blog_app:detail")

    def form_valid(self, form):
        post_pk = self.kwargs['pk']
        post = get_object_or_404(models.Post, pk=post_pk)
        form.instance.author = self.request.user

        # 紐づく記事を設定する
        comment = form.save(commit=False)
        comment.post = post
        comment.save()

        # 記事詳細にリダイレクト
        return redirect('blog_app:detail', pk=post_pk)



@login_required
def like(request, *args, **kwargs):
    post = models.Post.objects.get(id=kwargs['pk'])
    is_like = models.Like.objects.filter(user=request.user).filter(post=post).count()
    if post.like_num == None:
        post.like_num == 0

    # unlike
    if is_like > 0:
        liking = models.Like.objects.get(post_id=kwargs['pk'], user=request.user)
        liking.delete()
        post.like_num -= 1
        post.save()
        return redirect(reverse_lazy('blog_app:detail', kwargs={'pk': kwargs['pk']}))
    # like


    post.like_num += 1
    post.save()
    like = models.Like()
    like.user = request.user
    like.post = post
    like.save()
    return redirect(reverse_lazy('blog_app:detail', kwargs={'pk': kwargs['pk']}))
