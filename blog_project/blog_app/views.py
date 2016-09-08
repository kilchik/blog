from django.http import HttpResponse
from django.template import loader
from .models import Article


def index(request):
    latest_article_list = Article.objects.order_by('-pub_date')[:10]
    template = loader.get_template('blog_app/index.html')
    context = {
        'latest_article_list': latest_article_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, article_id):
    template = loader.get_template('blog_app/detailed.html')
    context = {
        'article': Article.objects.get(id=article_id),
    }
    return HttpResponse(template.render(context, request))
