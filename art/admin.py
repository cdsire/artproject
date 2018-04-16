# coding:utf-8
# from django.contrib import admin
from .models import Tag, Art
from xadmin import views
import xadmin



class BaseSetting(object):
    # 主题修改,将主页面变成中文展示
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    # 整体配置
    site_title = '美文后台管理系统'
    site_footer = '我的python项目__cdsire'
    menu_style = 'accordion'    # 菜单折叠


class TagAdmin(BaseSetting):
    # 后台列表展示列
    list_display = ['t_name', 't_info', 't_createtime']
    # 后台列表查询条件
    search_fields = ['t_name', 't_createtime']
    # 通过时间查询后台列表
    list_filter = ['t_name', 't_info', 't_createtime']
    list_per_page = 10


class ArtAdmin(object):
    # 后台列表显示列
    list_display = ['a_title', 'a_info', 'a_content', 'a_img', 'a_addtime', 'a_updatetime']
    # 后台列表查询条件
    search_fields = ['a_title', 'a_info', 'a_content']
    # 后台列表通过时间查询
    list_filter = ['a_title', 'a_info', 'a_content', 'a_addtime']
    list_per_page = 20
    style_fields = {'a_content':'ueditor'}


xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(Tag, TagAdmin)
xadmin.site.register(Art, ArtAdmin)

# admin.site.register(Tag)
# admin.site.register(Art)
