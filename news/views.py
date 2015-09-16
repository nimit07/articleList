from .models import Articles
from django.views.generic import DeleteView, UpdateView, View, CreateView
from django.http import JsonResponse, HttpResponse
from .forms import UpdateArticle, CreateArticle
from django.shortcuts import redirect
import json


class AjaxResponseMixin(object):
    """
       Mixin to add AJAX support to a form.
       Must be used with an object-based FormView (e.g. CreateView)
       """

    def render_to_json_response(self, context, **response_kwargs):
        data = json.dumps(context)
        response_kwargs['content_type'] = 'application/json'
        return HttpResponse(data, **response_kwargs)

    def form_invalid(self, form):
        response = super(AjaxResponseMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return self.render_to_json_response(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super(AjaxResponseMixin, self).form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            return self.render_to_json_response(data)
        else:
            return response


# Create your views here.
class ArticlesList(View):
    http_methods_names = ['get']
    model = Articles
    template_name = 'articles_list.html'

    def get(self, request,):
        resultset = Articles.objects.all()
        results = [ob.as_article() for ob in resultset]

        return JsonResponse(results, safe=False)


class Articles_list_year_wise(View):
    http_methods_names = ['get']
    model = Articles
    template_name = 'articles_list.html'

    def get(self, request, year):
        if year:
            resultset = Articles.objects.filter(timestamp__year=year)
            results = [ob.as_article() for ob in resultset]
            return JsonResponse(results, safe=False)
        return JsonResponse('null', safe=False)


class Articles_list_month_wise(View):
    model = Articles
    http_methods_names = ['get']
    template_name = 'articles_list.html'

    def get(self, request, year, month):
        if year and month:
            resultset = Articles.objects.filter(timestamp__year=year, timestamp__month=month)
            results = [ob.as_article() for ob in resultset]
            return JsonResponse(results, safe=False)
        return JsonResponse('null', safe=False)


class ArticleDetail(View):
    model = Articles
    template_name = 'article_detail.html'

    def get(self, request, pk):
        if pk:
            resultset = Articles.objects.filter(pk=pk)
            result = [ob.as_article() for ob in resultset]
            return JsonResponse(result, safe=False)
        return JsonResponse('null', safe=False)


class ArticleUpdate(AjaxResponseMixin, UpdateView):
    model = Articles
    template_name = 'update_article.html'
    success_url = '/articles/'
    form_class = UpdateArticle
    # def get(self, request, pk):
    #     if pk:
    #         form = UpdateArticle(pk)
    #         return JsonResponse({'form': form})
    #
    # def put(self, request, ):
    #     form_class = UpdateArticle
    #     form = form_class(request.PUT)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('/articles/')


class ArticleCreate(AjaxResponseMixin, CreateView):
    model = Articles
    template_name = 'create_article.html'
    form_class = CreateArticle
    success_url = '/articles/'


class ArticleDelete(DeleteView):
    model = Articles
    template_name = 'delete_article.html'
    success_url = '/articles/'
