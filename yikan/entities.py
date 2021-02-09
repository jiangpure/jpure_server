# -*- coding:utf-8 -*-
from yikan.models import Devices


class BaseRequest(object):
    def __init__(self):
        # 时间戳
        self.time = 0
        # 签名
        self.sign = ""


class BaseResponse(object):
    def __init__(self, code=0, msg="", data=None, sign=""):
        # 状态码
        self.code = code
        # 状态信息
        self.msg = msg
        # 数据
        self.data = data
        # 签名
        self.sign = sign


class InitRequest(BaseRequest):
    def __init__(self):
        super().__init__()
        # 包名
        self.package_name = ""
        # 版本名
        self.version_name = ""
        # 版本号
        self.version_code = 0
        # app签名
        self.app_sign = ""
        # 渠道标识
        self.ad_ver = ""
        # 设备信息
        self.device_info = Devices
        # 网络类型
        self.net_type = ""


class InitResponse(object):
    def __init__(self, access_token="", is_login=False, is_debug=False, is_show_dev_info=True,
                 is_auto_check_update=True, is_ban=False, ext=""):
        super().__init__()
        # token
        self.access_token = access_token
        # 是否需要登录
        self.is_login = is_login
        # 是否是debug模式
        self.is_debug = is_debug
        # 是否显示开发者信息
        self.is_show_dev_info = is_show_dev_info
        # 是否自动检查更新
        self.is_auto_check_update = is_auto_check_update
        # 是否禁止进入
        self.is_ban = is_ban
        # ext
        self.ext = ext


class UpdateRequest(BaseRequest):
    def __init__(self):
        super().__init__()
        # token
        self.access_token = ""
        # 版本号
        self.version_code = 0
        # app签名
        self.app_sign = ""
        # 渠道标识
        self.ad_ver = ""


class UpdateResponse(object):
    def __init__(self, **kwargs):
        # 新版code
        self.new_version_code = kwargs["new_version_code"]
        # 新版Name
        self.new_version_name = kwargs["new_version_name"]
        # app的签名
        self.app_sign = kwargs["app_sign"]
        # apk大小
        self.apk_size = kwargs["apk_size"]
        # apk的md5值
        self.apk_md5 = kwargs["apk_md5"]
        # 弹窗配置
        self.pop_config = kwargs["pop_config"]
        # 新版apk地址
        self.new_apk_url = kwargs["new_apk_url"]
        # 透传参数
        self.ext = kwargs["ext"]


class NoticeRequest(BaseRequest):
    def __init__(self):
        super().__init__()
        # token
        self.access_token = ""
        # 本地公告最后的版本
        self.last_ver = 0
        # app版本号
        self.version_code = ""
        # 渠道标识
        self.ad_ver = ""
        # 时间戳
        self.time = 0

class NoticeResponse(object):
    def __init__(self,**kwargs):
        super().__init__()
        # 公告类型， 0：普通 1：web 2：下载 3:图片
        self.type = kwargs.get("type", 0)
        # web或者图片的链接,其他则为空
        self.url = kwargs.get("url", "")
        # 公告的版本
        self.ver = kwargs["ver"]
        # 弹出次数，-1为每次打开都弹出
        self.times = kwargs.get("times", 1)
        # 弹窗配置
        self.pop_config = kwargs["pop_config"]


class SourceRequest(BaseRequest):
    def __init__(self):
        super().__init__()
        # token
        self.access_token = ""
        # apk版本名
        self.version_name = ""
        # apk版本号
        self.version_code = ""
        # 渠道标识
        self.ad_ver = ""


class SourceResponse(BaseResponse):
    def __init__(self):
        super().__init__()
        # 新版code
        self.new_version_code = 0
        # md5
        self.file_md5 = ""
        # 弹窗配置
        self.pop_config = PopConfig
        # 新资源文件地址
        self.update_url = ""


class PopConfig(object):
    def __init__(self, **kwargs):
        self.tag = kwargs.get("tag", "tag")
        self.width_percent = kwargs.get("width_percent", 0.8)
        self.height_percent = kwargs.get("height_percent", 0.5)
        self.dim_amount = kwargs.get("dim_amount", 0.3)
        self.title = kwargs.get("title", "Title")
        self.confirm_txt = kwargs.get("confirm_txt", "confirm")
        self.cancel_txt = kwargs.get("cancel_txt", "cancel")
        self.enforce = kwargs.get("enforce", False)
        self.content = kwargs.get("content", "")

# class PopConfig(object):
#     def __init__(self):
#         self.tag = ""
#         self.width_percent = 0.8
#         self.height_percent = 0.5
#         self.dim_amount = 0.5
#         self.title_txt = ""
#         self.confirm_txt = ""
#         self.cancel_txt = ""
#         self.enforce = False
#         self.content_detail = ""
