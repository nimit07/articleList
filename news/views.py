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
    def get_context_data(self, **kwargs):
        context=super(ArticlesList,self).get_context_data(**kwargs)
        year=self.kwargs.get('year', None)
        month=self.kwargs.get('month',None)
        if month and year:
            date_list=Articles.objects.filter(timestamp__month=month,timestamp__year=year)
        elif year:
            date_list=Articles.objects.filter(timestamp__year=year)
        else:
            date_list=Articles.objects.all()
        #for years in date_list:
            #context['list']+=Articles.objects.filter(timestamp__year=years.year)
        resultset=date_list
        results = [ob.as_article() for ob in resultset]
        context['list']=json.dumps(results)

        return context
