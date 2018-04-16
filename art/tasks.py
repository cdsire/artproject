#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'po'
__mtime__ = '18-4-16'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
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
"""
from __future__ import absolute_import
import time
from django.core.mail import send_mail
from celery.utils.log import get_task_logger
from artproject.celery import app

from django.core.mail import send_mail

from art.utils.send_mail import pack_html, send_email

@app.task
def tsend_email():
   url = "http://1000phone.com"
   receiver = 'zhouguangyou@1000phone.com'
   content = pack_html(receiver, url)
   # content = 'this is email content.'
   send_email(receiver, content)
   print('send email ok!')


@app.task
def add(x, y):
   return x+y