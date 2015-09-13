from django.shortcuts import render
from .models import Articles
from django.views.generic import ListView,DeleteView,DetailView,UpdateView,CreateView
import json
from django.core import serializers
from django.shortcuts import render_to_response
from  .forms import UpdateArticle,CreateArticle

# Create your views here.
class ArticlesList(ListView):
    model=Articles
    template_name='articles_list.html'

class Articles_list_year_wise(ListView):
    model=Articles
    template_name='articles_list.html'
    def get_queryset(self):
        if self.kwargs['year']:
            return self.model.objects.filter(timestamp__year=self.kwargs['year'])
class Articles_list_month_wise(ListView):
    model=Articles
    template_name='articles_list.html'
    def get_queryset(self):
        if self.kwargs['month'] and self.kwargs['year']:
            return self.model.objects.filter(timestamp__month=self.kwargs['month'],timestamp__year=self.kwargs['year'])
class ArticleDetail(DetailView):
    model=Articles
    template_name='article_detail.html'

class ArticleUpdate(UpdateView):
    model=Articles
    template_name='update_article.html'
    form_class=UpdateArticle
    success_url='/articles/'
class ArticleCreate(CreateView):
    model=Articles
    template_name='create_article.html'
    form_class=CreateArticle
    success_url='/articles/'
class ArticleDelete(DeleteView):
    model=Articles
    template_name='delete_article.html'
    success_url='/articles/'
