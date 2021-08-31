from django.shortcuts import render
from Heapp.detectdevice import DetectMobileBrowser
from Heapp.models import User, Comment
from django.http import HttpResponse, JsonResponse


# Create your views here.
def main_index(request):
    # DMB = DetectMobileBrowser()
    # if DMB.isMobile(request):
    #     return render(request, 'Heapp/Mobileindex.html')
    # else:
    #     return render(request, 'Heapp/PCindex.html')

    if request.session.has_key("is_login") and request.session['is_login']==True:
        res = {
            'userdisplay': "block",
            'logindisplay': "none",
            'username': str("你好, "+request.session['username']),
        }
        return render(request, 'Heapp/PCindex.html', res)
    else:
        res = {
            'userdisplay': "none",
            'logindisplay': "block",
        }
        return render(request, 'Heapp/PCindex.html', res)

def register(request):
    try:
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        user = User.objects.filter(username=username)
        if len(user)==0:
            request.session['username'] = username
            request.session['is_login'] = True
            request.session.set_expiry(300)
            User.objects.create(username=username, password=password)
            result={
                'status': True,
                'username': username,
            }
        else:
            result={
                'status': False,
            }
    except:
        result={
            'status': False,
        }
    return JsonResponse(result)

def login(request):
    try:
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        #print(username, password)
        user = User.objects.get(username=username)
        if user.password == password:
            request.session['username']=username
            request.session['is_login']=True
            request.session.set_expiry(300)
            result={
                'status': True,
                'username': username,
            }
        else:
            result={
                'status': False,
            }
    except:
        result={
            'status': False,
        }
    return JsonResponse(result)

def logout(request):
    request.session.flush()
    res = {
        'userdisplay': "none",
        'logindispaly': "block",
    }
    return JsonResponse(res)
