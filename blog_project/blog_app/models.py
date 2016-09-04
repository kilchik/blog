from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=200)
    cut = models.TextField()
    rest_text = models.TextField()
    pub_date = models.DateTimeField('date published')
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
