# -*- coding:utf-8 -*-
from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import User
from .models import UserDevices
from .models import UserToken
from .models import Notice
from .models import Devices
from .models import UpdateInfo
from .models import PopConfig

admin.site.register(User)
admin.site.register(UserDevices)
admin.site.register(UserToken)
admin.site.register(Notice)
admin.site.register(Devices)
admin.site.register(UpdateInfo)
admin.site.register(PopConfig)