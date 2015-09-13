
from django.conf.urls import include, url
from .views import ArticleCreate,ArticleDelete,ArticleDetail,Articles_list_month_wise,Articles_list_year_wise,ArticlesList,ArticleUpdate





urlpatterns = [
url(r'^(?P<year>[0-9]{4})/$',Articles_list_year_wise.as_view(),name='articles-list-year_wise'),
url(r'^$',ArticlesList.as_view(),name='articles-list'),
url(r'^(?P<year>[0-9]{4})/(?P<month>[0-1]{1}[0-9]{1})/$',Articles_list_month_wise.as_view(),name='articles-list-month_wise'),
url(r'^(?P<pk>[0-9]+)/$',ArticleDetail.as_view(),name='article-detail_by_id'),
url(r'^update_article/(?P<pk>[\w-]+)$',ArticleUpdate.as_view(),name='update_article'),
url(r'^create_article/$',ArticleCreate.as_view(),name='create_article'),
url(r'^delete_article/(?P<pk>[\w-]+)$',ArticleDelete.as_view(),name='delete_article')
]
