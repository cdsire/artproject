# coding:utf-8
"""
Django settings for artproject project.

Generated by 'django-admin startproject' using Django 1.11.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^5tp5bqkdh#3*!bqo=b5m62o(b#1@774a0=+-#zl6@41-00dpx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'art',
    'xadmin',
    'crispy_forms',
    'DjangoUeditor',
    'djcelery',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'artproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'artproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'artproject',
        'HOST':'127.0.0.1',
        'PORT':3306,
        'USER':'root',
        'PASSWORD':'123456',
        'charset':'utf8',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'art/static/')

MEDIA_ROOT = os.path.join(BASE_DIR, 'art/static')
MEDIA_URL = '/static/uploads/'

# 媒体文件：用户上传的文件，叫做media
# 静态文件：css,js，image等 叫做static

# 处理日志
#########################
## Django Logging  BEGIN
#########################
#LOGGING_DIR 日志文件存放目录
LOGGING_DIR = "./logs"
if not os.path.exists(LOGGING_DIR):
    os.mkdir(LOGGING_DIR)

import logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {	# 标准格式
            'format': '[%(levelname)s][%(asctime)s][%(filename)s][%(funcName)s][%(lineno)d]> %(message)s'
        },
        'simple': {	# 简单格式
            'format': '[%(levelname)s]> %(message)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file_handler': {
             'level': 'INFO',    # info级别比debug高，只会显示比设置的级别高的对应日志
             'class': 'logging.handlers.TimedRotatingFileHandler',
             'filename': '%s/django.admin.log' % LOGGING_DIR,
             'formatter':'standard'
        }, # 用于文件输出
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
             'formatter':'standard'
        },
    },
    'loggers': {
        'django': {
        	# 如果不写'console'，则不会在终端显示日志，只会存到文件
            'handlers': ['console','file_handler'],
            'level':'DEBUG',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
    }
}
#########################
## Django Logging  END
#########################



#############################
# celery 配置信息 start
#############################
import djcelery
djcelery.setup_loader()
BROKER_URL = 'redis://127.0.0.1:6379/1'	# 1代表redis服务的第一个槽位
CELERY_IMPORTS = ('art.tasks')
CELERY_TIMEZONE = 'Asia/Shanghai'	# 时区写错定时器会失效
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
from celery.schedules import crontab
from celery.schedules import timedelta

CELERYBEAT_SCHEDULE = {    #定时器策略
    #定时任务一：　每隔30s运行一次
    u'测试定时器1': {
        "task": "art.tasks.tsend_email",	# 定时让任务发送邮件
        #"schedule": crontab(minute='*/2'),  # or 'schedule': timedelta(seconds=3),
        "schedule":timedelta(seconds=30),
        "args": (),
    },
}
#############################
# celery 配置信息 end
#############################

