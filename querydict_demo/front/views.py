from django.shortcuts import render
from django.http import HttpResponse
from django.http.request import QueryDict
from django.views.decorators.http import require_http_methods

def index(request):
    # username = request.GET['username']
    username = request.GET.get('p',default=1)
    print(username)
    return HttpResponse('success')

@require_http_methods(['GET','POST'])
def add_article(request):
    if request.method == 'GET':
        return render(request,'add_article.html')
    else:
        title = request.POST.get("title")
        content = request.POST.get('content')
        tags = request.POST.getlist('tags')
        print('title:',title)
        print('content:',content)
        print('tags:',tags)
        return HttpResponse("success")

