from django.db import models


# legacy table -> articles schema
class Tag(models.Model):
    id = models.IntegerField(primary_key=True)
    tag_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tags'
