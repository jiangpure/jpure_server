# -*- coding:utf-8 -*-
from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)  # id
    name = models.CharField(max_length=100)  # 账号名
    password = models.CharField(max_length=100)  # 密码（md5）
    last_login_time = models.BigIntegerField()  # 最后登陆时间
    last_update_time = models.BigIntegerField()  # 修改时间

    def __unicode__(self):  # __str__ on Python 3
        return self.name


class UserDevices(models.Model):
    user_id = models.IntegerField()  # user_id
    devices = models.TextField()  # 设备列表

    def __unicode__(self):  # __str__ on Python 3
        return self.user_id


class UserToken(models.Model):
    user_id = models.IntegerField()  # user_id
    token = models.TextField()  # 登录的token
    update_time = models.BigIntegerField()  # 最近修改时间
    expired_time = models.BigIntegerField()  # token过期时间

    def __unicode__(self):  # __str__ on Python 3
        return self.user_id


class Devices(models.Model):
    id = models.AutoField(primary_key=True)  # id
    imei = models.CharField(max_length=100)  # imei
    oaid = models.CharField(max_length=100) # oaid
    name = models.CharField(max_length=100) # 设备名称
    mac = models.CharField(max_length=100) # mac地址
    product = models.CharField(max_length=100)  # 产品型号
    os = models.CharField(max_length=100)  # 系统
    cpu = models.CharField(max_length=100)  # 支持的cpu架构
    api = models.IntegerField()  # 系统API版本
    sys_ver = models.CharField(max_length=100)  # 系统版本
    emulator = models.BooleanField()  # 是否是模拟器
    screen = models.CharField(max_length=100)  # 屏幕尺寸
    last_time = models.BigIntegerField()  # 最近使用时间

    def __unicode__(self):  # __str__ on Python 3
        return self.id


class PopConfig(models.Model):
    id = models.AutoField(primary_key=True)  # id
    tag = models.CharField(max_length=100)  # tag
    width_percent = models.FloatField()  # 宽占比
    height_percent = models.FloatField()  # 高占比
    dim_amount = models.FloatField()  # 阴影百分比
    enforce = models.BooleanField()  # 是否强制弹出不可取消
    title = models.CharField(max_length=100)  # 标题
    content = models.TextField()  # 内容
    confirm_txt = models.CharField(max_length=100)  # 确认提示
    cancel_txt = models.CharField(max_length=100)  # 取消提示

    def __unicode__(self):  # __str__ on Python 3
        return self.id


class Notice(models.Model):
    id = models.AutoField(primary_key=True)  # id
    ver = models.BigIntegerField()  # 版本
    type = models.IntegerField()  # 类型
    url = models.CharField(max_length=200)  # 内容url
    pop_config = models.ForeignKey(PopConfig, on_delete=models.CASCADE)  # 弹窗配置
    times = models.IntegerField()  # 弹出次数
    create_time = models.DateTimeField(auto_now_add=True, editable=False)  # 创建时间
    author = models.CharField(max_length=100)  # 创建者

    def __unicode__(self):  # __str__ on Python 3s
        return self.id


class UpdateInfo(models.Model):
    id = models.AutoField(primary_key=True)  # id
    pop_config = models.ForeignKey(PopConfig, on_delete=models.CASCADE)  # 弹框信息
    new_version_code = models.BigIntegerField()  # 新版本号
    new_version_name = models.CharField(max_length=100)  # 新版本名
    app_sign = models.CharField(max_length=200)  # app签名的md5
    apk_md5 = models.CharField(max_length=200)  # 文件的md5值
    apk_size = models.IntegerField()  # 文件的大小
    new_apk_url = models.CharField(max_length=200)  # 新版下载地址
    ext = models.TextField()  # 透传参数
    author = models.CharField(max_length=100)  # 创建者
    create_time = models.DateTimeField(auto_now_add=True, editable=False)  # 创建时间
    last_update_time = models.DateTimeField(auto_now=True)  # 最后修改时间


    def __unicode__(self):  # __str__ on Python 3
        return self.id