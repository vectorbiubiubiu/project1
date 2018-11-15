#encoding: utf-8

from django.http import HttpResponse,JsonResponse
import json

def index(request):
    response = HttpResponse('<h1>知了课堂</h1>',content_type='text/plain;charset=utf-8')
    # response.status_code = 400
    response['X-Token'] = 'zhiliao'
    # response.content = '知了课堂'
    response.write('zhiliao')
    return response

def jsonresponse_view(request):
    persons = [
        {
        'username': 'zhiliao',
        'age': 18,
        'height': 180
        },
        {
            'username': 'zhiliao1',
            'age': 20,
            'height': 180
        }
    ]
    # person_str = json.dumps(person)
    # response = HttpResponse(person_str,content_type='application/json')
    # return response
    response = JsonResponse(persons,safe=False)
    return response
