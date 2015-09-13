from django.shortcuts import render
from .models import Articles
from django.views.generic import ListView,DeleteView,DetailView,UpdateView,CreateView
import json
from django.core import serializers
from django.shortcuts import render_to_response

# Create your views here.
class ArticlesList(ListView):
    model=Articles
    template_name='articles_list.html'
    def get_queryset(self):
        if self.kwargs['month'] and self.kwargs['year']:
            return self.model.objects.filter(timestamp__month=self.kwargs['month'],timestamp__year=self.kwargs['year'])
        elif self.kwargs['year']:
            return self.model.objects.filter(timestamp__year=self.kwargs['year'])
        else:
            return self.model.objects.all()
    def get_context_data(self, **kwargs):
        context=super(ArticlesList,self).get_context_data(**kwargs)
        return context
    class ArticleDetail(DetailView):
        model=Articles
