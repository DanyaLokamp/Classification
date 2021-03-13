from rest_framework import serializers
from .models import Article, Tag


class ArticleSerializer(serializers.ModelSerializer):
    date_published = serializers.SerializerMethodField()
    tag = serializers.SerializerMethodField()

    def get_date_published(self, obj):
        return obj.date_published.date()

    def get_tag(self, obj):
        return obj.tag.tag_name;

    class Meta:
        model = Article
        fields = ('id', 'article_id', 'author', 'title', 'date_published', 'tag', 'article_text', 'url')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'tag_name')
