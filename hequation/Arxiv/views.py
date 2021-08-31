from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
import requests
import re
from lxml import etree
from lxml import html
# Create your views here.

def arxiv(request):
    # newurl = "https://arxiv.org/"
    # arxivResponse = requests.get(newurl)
    # arxivHtml = arxivResponse.text
    # return HttpResponse(arxivHtml)
    return render(request, "Arxiv/arxiv.html", {})

def multi(request):
    group = request.GET.get("group")
    return redirect("/search/"+group)

#无参数请求 直接返还搜索页
#有参数请求 返还结果页
def search(request):
    url = request.get_full_path()
    newurl = "https://arxiv.org"+url
    print(newurl)
    arxivResponse = requests.get(newurl)
    arxivHtml = arxivResponse.text

    if '?' not in newurl:
        return HttpResponse(arxivHtml)

    arxivHtml = arxivResponse.content.decode()
    root = etree.HTML(arxivHtml)

    #取出ol列表
    ol = root.xpath("//ol")[0]
    i1 = html.fromstring("<input name=\"selectAllBox\" type=\"checkbox\" onclick=\"selectAllCheckBox()\">All    ")
    i2 = html.fromstring("<input type=\"checkbox\" onclick=\"reverseAllCheckBox()\">Reverse    ")
    i3 = html.fromstring("<input type=\"button\" value=\"download\" class=\"button is-link is-small\" onclick=\"downloadChecked()\">")
    ol.insert(0, i3)
    ol.insert(0, i2)
    ol.insert(0, i1)

    lis = ol.xpath('//ol[@class="breathe-horizontal"]/li')
    for li in lis:
        title = li.xpath('./p[@class="title is-5 mathjax"]//text()')
        title = ''.join(title).replace('\n', '').lstrip(' ').strip(' ')
        href = li.xpath('./div/p/span/a/@href')[0]
        checkbox = html.fromstring("<input type=\"checkbox\" name=\"downloadCheckBox\" onclick=\"setSelectAllBox()\" value=\"" + href +".pdfHXL" + title  +".pdf"+"\"" +">")
        li.insert(0, checkbox)

    #插入js
    head = root.xpath("//head")[0]
    js0 = html.fromstring("<script src=\"https://unpkg.com/axios/dist/axios.min.js\"></script>")
    js1 = html.fromstring("<script src=\"/static/js/download.js\"></script>")
    head.insert(0, js1)
    head.insert(0, js0)
    return HttpResponse(html.tostring(root).decode())

def test(request):
    res={}
    return render(request, "Arxiv/test.html", res)
