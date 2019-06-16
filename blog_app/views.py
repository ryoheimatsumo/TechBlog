from django.shortcuts import render
from django.views.generic import (View,TemplateView,
                                    ListView,DetailView,
                                    CreateView,UpdateView,DeleteView)
from django.urls import reverse_lazy
from . import models
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.
@method_decorator(login_required, name='dispatch')
class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School
    # school_list

@method_decorator(login_required, name='dispatch')
class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'blog_app/school_detail.html'

@method_decorator(login_required, name='dispatch')
class SchoolCreateView(CreateView):
    fields = ('name','principal','location')
    model = models.School

@method_decorator(login_required, name='dispatch')
class SchoolUpdateView(UpdateView):
    fields = ('name','principal')
    model = models.School

@method_decorator(login_required, name='dispatch')
class SchoolDeleteView(DeleteView):
    model=models.School
    success_url = reverse_lazy("blog_app:list")
