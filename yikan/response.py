# -*- coding:utf-8 -*-
from django.db.models import Q
from django.forms import model_to_dict

from yikan.entities import BaseResponse, InitResponse, PopConfig, UpdateResponse, NoticeResponse
from yikan.models import Devices, UpdateInfo, Notice


def createInitResponse(initRequest):
    # 保存设备信息
    device = Devices(last_time=initRequest.time, **initRequest.device_info)
    factor_filter = None
    if (device.oaid != ""): factor_filter = Q(oaid=device.oaid)
    if (device.imei != ""): factor_filter = Q(imei=device.imei)
    result = Devices.objects.filter(factor_filter)
    if (result.count() > 0):
        result.update(last_time=initRequest.time, **initRequest.device_info)
    else:
        device.save()
    return BaseResponse(code=200, msg="success", data=InitResponse(access_token="agdg2cs71hklacvbjpo9", is_debug=True).__dict__,
                        sign="afh1012h3g87yigf")


def createUpdateResponse(updateRequest):
    """
    构建更新返回数据
    :param updateRequest: 更新请求
    :return:
    """
    result = UpdateInfo.objects.filter(new_version_code__gte=updateRequest.version_code)
    if (result.count() > 0):
        config = PopConfig(**model_to_dict(result[result.count()-1].pop_config))
        # 直接传字典不要传对象
        kwargs = model_to_dict(result[result.count()-1])
        kwargs["pop_config"] = config.__dict__
        response = UpdateResponse(**kwargs)
        return BaseResponse(code=200, msg="success", data=response.__dict__, sign="afh1012h3g87yigf")
    else:
        config = PopConfig()
        response = UpdateResponse(pop_config=config.__dict__)
        return BaseResponse(code=200, msg="success", data=response.__dict__, sign="afh1012h3g87yigf")

def createNoticeResponse(noticeRequest):
    result = Notice.objects.filter(ver__gte=noticeRequest.last_ver)
    if (result.count() > 0):
        config = PopConfig(**model_to_dict(result[0].pop_config))
        # 直接传字典不要传对象
        kwargs = model_to_dict(result[0])
        kwargs["pop_config"] = config.__dict__
        response = NoticeResponse(**kwargs)
        return BaseResponse(code=200, msg="success", data=response.__dict__, sign="afh1012h3g87yigf")
    else:
        config = PopConfig()
        response = NoticeResponse(pop_config=config.__dict__, ver=202102051158)
        return BaseResponse(code=200, msg="success", data=response.__dict__, sign="afh1012h3g87yigf")