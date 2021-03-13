from django.urls import path, include, re_path
from . import views
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

# router = routers.DefaultRouter()
# router.register('articles', views.ArticleView, basename="Article")
# router.register('tags', views.TagView, basename='Tag')

# urlpatterns = [
#     path('', include(router.urls))
# ]

urlpatterns = format_suffix_patterns([
    path('', views.ArticleList.as_view()),
    # path('articles/',
    #      views.ArticleList.as_view(),
    #      name='article-list'),
    path('articles/',
         views.ArticleListByDates.as_view({'get': 'list'})),
    path('articles/<int:pk>/',
         views.ArticleDetail.as_view(),
         name='article-detail'),
    path('tags/',
         views.TagView.as_view({'get': 'list'}))
])