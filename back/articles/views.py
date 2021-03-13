from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework import generics
from rest_framework.views import APIView

from .models import Article, Tag
from .serializers import ArticleSerializer, TagSerializer


class ArticleList(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetail(generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleListByDates(viewsets.ViewSet):
    def list(self, request):
        date_start = request.GET['start']
        date_end = request.GET['end']
        queryset = Article.objects.filter(date_published__range=[date_start, date_end])
        serializer = ArticleSerializer(queryset, many=True)
        return Response(serializer.data)



class TagView(viewsets.ModelViewSet):
    def create(self, request):
        try:
            serializer = TagSerializer(data=self.request.data)
            if serializer.is_valid():
                serializer.save()
                return Response('Tag was successfully created.')
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response('Something went wrong...', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        queryset = Tag.objects.all()
        serializer = TagSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Tag.objects.all()
        tag = get_object_or_404(queryset, pk=pk)
        serializer = TagSerializer(tag)
        return Response(serializer.data)
