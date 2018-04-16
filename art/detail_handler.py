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

from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Art, Tag


'''
详情页面功能：
    接口URL：　/art/detail?id=7
    方法：GET
    输入参数说明：文章id,点击某个具体的文章，传入文章id
    输出：渲染详情页面
'''
def DetailHandler(request):
    art_id = request.GET.get('id', None)
    # 如果没有文章，返回首页，有文章，返回详情页
    if art_id == None:
        return HttpResponseRedirect('/art/index')
    else:
        art = Art.objects.get(id=int(art_id))
        context = {'art':art}
        return render(request, 'home/detail.html', context=context)