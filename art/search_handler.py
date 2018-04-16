#!/usr/bin/env python  
# encoding: utf-8  

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from art.models import Art, Tag
from django.db.models import Q

import logging

'''
函数名： SearchHandler
接口URL：/art/search?key=XXX&page=1
方法：GET
输入参数说明：
    key: 搜索的关键词
    page: 获取第几页
输出：渲染搜索列表页面
'''

def SearchHandler(request):
	key = request.GET.get('key', '')	# 搜索关键词
	page = request.GET.get('page', 1)	#url中显示的页数
	total = 0
	logger = logging.getLogger('django')
	logger.info('searchHandler request handler begin...')
	#　如果关键词为空，则显示首页
	if key == "":
		return HttpResponseRedirect('/art/index')
	else:
		page = int(page)
		#　Q查询有关键词的标题、内容、简介
		art_sets = Art.objects.filter(Q(a_title__contains=str(key))
									| Q(a_content__contains=str(key))
									| Q(a_info__contains=str(key))).distinct()
		total = art_sets.count()	#　统计搜到的数量
		logger.debug('query total:' + str(total))

		shownum = 10	#　每页显示１０条搜索到的数据
		import math
		pagenum = int(math.ceil(total / shownum))	#　搜索到的总页数
		#　自定义初始化展示内容
		context = dict(
			pagenum=pagenum,
			total=total,
			prev=1,	#上一页
			next=1,	#下一页
			pagerange=range(1, 2),	#每页只显示１页
			data=[],
			url=request.path,
			key=key,
			page=1,
		)
		if page < 1:
			return render(request, "home/search.html", context=context)
		if page > pagenum:
			return render(request, "home/search.html", context=context)
		offset = (page - 1) * shownum
		art_list = Art.objects.filter(Q(a_title__contains=str(key))
				   | Q(a_content__contains=str(key))
				   | Q(a_info__contains=str(key))).distinct()

		data = art_list[offset:(shownum + offset)]	#　当前显示的搜索内容
		btnnum = 5	#　最多显示５页

		if btnnum > pagenum:	#　搜索到的页数小于５时,起始页＝１,终止页＝搜索到的页数
			firstpage = 1
			lastpage = pagenum
		else:	#　当搜索到的页数大于等于５时：如果要显示第一页，则起始页＝１,终止页＝５;如果不是显示第一页,则起始页＝page-2,终止页＝page+btnnum-3
			if page == 1:
				firstpage = 1
				lastpage = btnnum
			else:
				firstpage = page - 2
				lastpage = page + btnnum - 3

				if firstpage < 1:	# 如果page<3,则起始页还是等于１
					firstpage = 1
				if lastpage > pagenum:	#　如果搜索到的页数小于终止页，则终止页＝搜索到的页数
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
			key=key,
			page=page
		)
		return render(request, "home/search.html", context=context)

