from django.db import models
from markdown import markdown


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=200)
    cut_md = models.TextField()
    cut_html = models.TextField(editable=False)
    rest_text_md = models.TextField()
    rest_text_html = models.TextField(editable=False)
    pub_date = models.DateTimeField('date published')
    tags = models.ManyToManyField(Tag)

    def save(self):
        self.cut_html = markdown(self.cut_md)
        self.rest_text_html = markdown(self.rest_text_md)
        super(Article, self).save()

    def __str__(self):
        return self.title
