#encoding: utf-8
from django.http import HttpResponse
from datetime import datetime
from django.utils.timezone import make_aware

def index(request):
    response = HttpResponse("index")
    expires = datetime(year=2018,month=5,day=9,hour=20,minute=0,second=0)
    expires = make_aware(expires)
    response.set_cookie('user_id','abc',expires=expires,max_age=180,path='/cms/')
    return response

def delete_cookie(request):
    response = HttpResponse('delete')
    response.delete_cookie('username')
    return response

def my_list(request):
    cookies = request.COOKIES
    username = cookies.get('user_id')
    return HttpResponse(username)

def cms_view(request):
    cookies = request.COOKIES
    username = cookies.get('user_id')
    return HttpResponse(username)

from datetime import timedelta
def session_view(request):
    # expiry = datetime(year=2018,month=6,day=1,hour=0,minute=0,second=0)
    # expiry = make_aware(expiry)
    expiry = timedelta(days=2)
    request.session.set_expiry(expiry)
    return HttpResponse('session view')

def get_session_view(request):
    username = request.session.get('username')
    print(username)
    return HttpResponse('get session view')
