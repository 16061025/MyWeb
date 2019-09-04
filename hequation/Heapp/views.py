from django.shortcuts import render
from Heapp.detectdevice import DetectMobileBrowser
# Create your views here.
def main_index(request):
    # DMB = DetectMobileBrowser()
    # if DMB.isMobile(request):
    #     return render(request, 'Heapp/Mobileindex.html')
    # else:
    #     return render(request, 'Heapp/PCindex.html')
    return render(request, 'Heapp/PCindex.html')
def regiter(request):
    return

def login(request):
    return

