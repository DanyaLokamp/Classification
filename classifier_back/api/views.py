import pickle
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets
from django.shortcuts import get_object_or_404

from .models import Tag

file = open("classifierModel.txt", "rb")
classifier = pickle.load(file)
file.close()


class ArticleView(viewsets.ModelViewSet):
    def create(self, request):
        try:
            article_text = request.data.get('article_text', None)
            if article_text is not None and article_text != '':
                tag_number = classifier.predict([article_text])
                queryset = Tag.objects.all()
                tag = get_object_or_404(queryset, pk=tag_number)
                json_response = {"class": tag.tag_name}
                return Response(json_response)
            else:
                return Response('params', status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response('Something went wrong...', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#
# @api_view(["POST"])
# def predict(request):
#     try:
#         article_text = request.data.get('article_text', None)
#         if article_text is not None and article_text != '':
#             tag_number = classifier.predict([article_text])
#             queryset = Tag.objects.all()
#             tag = get_object_or_404(queryset, pk=tag_number)
#             json_response = {"class": tag.tag_name}
#             return Response(json_response)
#         else:
#             return Response('article_text is either empty or not specified', status=status.HTTP_400_BAD_REQUEST)
#     except Exception:
#         return Response('Something went wrong', status=status.HTTP_500_INTERNAL_SERVER_ERROR)