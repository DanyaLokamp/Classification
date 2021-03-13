from django.db import models


class Tag(models.Model):
    tag_name = models.CharField(max_length=50, default='')

    def __str__(self):
        return str(self.pk) + ': ' + self.tag_name

    class Meta:
        db_table = "tags"


class Article(models.Model):
    article_id = models.CharField(max_length=50, default='')
    author = models.CharField(max_length=50, default='')
    title = models.CharField(max_length=500, default='')
    date_published = models.DateTimeField(null=True, default=None)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, default=1)
    article_text = models.CharField(max_length=5000, default='')
    url = models.CharField(max_length=100, default='')

    def __str__(self):
        return str(self.date_published.date()) + ' ' + self.author + ': ' + self.title

    class Meta:
        db_table = "articles"



