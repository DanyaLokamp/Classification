from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'predict', views.ArticleView, basename='Article')

urlpatterns = [
    path('', include(router.urls)),
]
# urlpatterns = [
#     path('predict/',
#          views.ArticleView.as_view({'post': 'create'}))
#     #path('predict', views.predict),
# ]