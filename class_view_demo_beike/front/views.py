from django.shortcuts import render
from django.views.generic import ListView
from .models import Article
from django.http import HttpResponse
from django.core.paginator import Paginator

class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'
    paginate_by = 10
    context_object_name = 'articles'
    ordering = 'create_time'
    page_kwarg = 'page'
    
    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        paginator = context.get('paginator')
        page_obj = context.get('page_obj')
        pagination_data = self.get_pagination_data(paginator,page_obj,2)
        context.update(pagination_data)
        return context

    def get_pagination_data(self,paginator,page_obj,around_count):
        # 1,2,[3],4,5
        page_range = paginator.page_range
        current_page = page_obj.number
        left_has_more = False
        right_has_more = False
        num_pages = paginator.num_pages

        if current_page <= around_count + 2:
            left_pages = range(1,current_page)
        else:
            left_pages = range(current_page-around_count,current_page)
            left_has_more = True


        if current_page >= num_pages - around_count - 1:
            right_pages = range(current_page+1,num_pages+1)
        else:
            right_pages = range(current_page+1,current_page+around_count+1)
            right_has_more = True

        return {
            'left_pages': left_pages,
            'right_pages': right_pages,
            'left_has_more': left_has_more,
            'right_has_more': right_has_more,
            'current_page': current_page,
            'num_pages': paginator.num_pages
        }

    def get_queryset(self):
        return Article.objects.filter(id__lte=200)



def add_article(request):
    articles = []
    for x in range(0,102):
        article = Article(title='title %s'%x,content='bbb')
        articles.append(article)
    Article.objects.bulk_create(articles)
    return HttpResponse("add article success")
