# coding:utf-8
'''
   ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
'''
import math
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Art, Tag


def IndexHandler(request):
    url = request.path
    # 当前页
    page = request.GET.get('page', 1)
    # 选择的标签
    t = request.GET.get('t', 0)
    page = int(page)
    t = int(t)

    total = 0
    if t == 0:
        art_set = Art.objects.all()
        total = art_set.count()
    else:
        tag_id = int('{0}'.format(t))
        art_set = Art.objects.filter(a_tag_id=tag_id)
        total = art_set.count()

    tags = Tag.objects.all()
    context = dict(
        pagenum = 1,
        total = 0,
        prev = 1,
        next = 1,
        pagerange = range(1,2),
        data = [],
        url = request.path,
        tags = tags,
        page = page,
        t = t
    )
    if total > 0:
        shownum = 20
        pagenum = int(math.ceil(total / shownum))
        if page < 1:
            url = request.path + '?page=1&t=1'
            return HttpResponseRedirect(url)
        if page > pagenum:
            url = request.path + '?page=%s&t=%s' % (pagenum, t)
            return HttpResponseRedirect(url)
        # 偏移量
        offset = (page - 1) * shownum
        if t == 0:
            data = Art.objects.all()[offset:shownum + offset]
        else:
            data = Art.objects.filter(a_tag_id=t)[offset:shownum + offset]
        btnum = 5
        if btnum > pagenum:
            firstpage = 1
            lastpage = pagenum
        else:
            if page == 1:
                firstpage = 1
                lastpage = btnum
            else:
                firstpage = page -2
                lastpage = page + btnum -3
                if firstpage < 1:
                    firstpage = 1
                if lastpage > pagenum:
                    lastpage = pagenum

        prev = page - 1
        next = page + 1
        if prev < 1:
            prev = 1
        if next > pagenum:
            next = pagenum
        context = dict(
            pagenum=pagenum,
            total=total,
            prev=prev,
            next=next,
            pagerange=range(firstpage, lastpage + 1),
            data=data,
            url=request.path,
            tags=tags,
            page=page,
            t=t
        )

    return render(request, 'home/index.html', context=context)

