# coding:utf-8
from django.db import models
from django.utils import timezone
from DjangoUeditor.models import UEditorField


# 标签表
class Tag(models.Model):
    t_name = models.CharField(max_length=255, verbose_name='标签名称')   # 帖子名称
    t_info = models.CharField(max_length=300, verbose_name='标签简介')   # 帖子信息
    # db_index是在数据库中创建索引
    t_createtime = models.DateTimeField(default=timezone.now, db_index=True, verbose_name='添加时间')    # 创建时间

    def __str__(self):
        return self.t_name

    class Meta:
        verbose_name_plural = '标签名称'
        verbose_name = '标签名称'


# 文章表
class Art(models.Model):
    a_title = models.CharField(max_length=255, verbose_name='文章标题')
    a_info = models.CharField(max_length=500, verbose_name='文章简介')
    # 使用富文本编辑器
    a_content = UEditorField(verbose_name='文章内容',
                             width=1000,
                             height=600,
                             imagePath='static/uploads/',
                             filePath='static/uploads/',
                             blank=True,
                             toolbars='full')
    # upload_to上传到‘uploads’,会自动创建到static静态文件中,还要去settings.py中设置静态文件路径
    a_img = models.ImageField(null=True, blank=True, upload_to='uploads', verbose_name='文章配图')

    a_addtime = models.DateTimeField(default=timezone.now, db_index=True, verbose_name='添加时间')
    a_updatetime = models.DateTimeField(default=timezone.now, db_index=True, verbose_name='修改时间')
    a_tag = models.ForeignKey(Tag)

    def __str__(self):
        return self.a_title

    class Meta:
        verbose_name_plural = '文章标题'
        verbose_name = '文章标题'
        ordering = ['-a_addtime']


