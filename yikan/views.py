import json

from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

from yikan.entities import InitRequest, UpdateRequest
from yikan.response import createInitResponse, createUpdateResponse, createNoticeResponse


@require_http_methods(["POST"])
def init(request):
    """
    初始化
    :param request:
    :return:
    """
    if request.META.get('HTTP_X_FORWARDED_FOR'):
        ip = request.META.get("HTTP_X_FORWARDED_FOR")
    else:
        ip = request.META.get("REMOTE_ADDR")
    print("ip:{0},content:{1}".format(ip, request.body))
    # 新建一个新的InitRequest对象
    initRequest = InitRequest()
    # 将字典转化为对象
    initRequest.__dict__ = json.loads(request.body)
    initResponse = createInitResponse(initRequest)
    print("response:"+json.dumps(initResponse.__dict__))
    return HttpResponse(json.dumps(initResponse.__dict__))


@require_http_methods(["POST"])
def check_update(request):
    """
    初始化
    :param request:
    :return:
    """
    update_body = json.loads(request.body)
    # # 新建一个新的InitRequest对象
    updateRequest = UpdateRequest()
    # # 将字典转化为对象
    updateRequest.__dict__ = update_body

    updateResponse = createUpdateResponse(updateRequest)
    print("response:" + json.dumps(updateResponse.__dict__))
    return HttpResponse(json.dumps(updateResponse.__dict__))

@require_http_methods(["POST"])
def get_notice(request):
    """
    初始化
    :param request:
    :return:
    """
    notice_body = json.loads(request.body)
    # # 新建一个新的InitRequest对象
    noticeRequest = UpdateRequest()
    # # 将字典转化为对象
    noticeRequest.__dict__ = notice_body

    noticeResponse = createNoticeResponse(noticeRequest)
    print("response:" + json.dumps(noticeResponse.__dict__))
    return HttpResponse(json.dumps(noticeResponse.__dict__))

@require_http_methods(["POST"])
def login(request):
    """
    登录
    :param request:
    :return:
    """
    return


@require_http_methods(["POST"])
def updateUserInfo(request):
    """
    更新用户信息
    :param request:
    :return:
    """
    return


@require_http_methods(["POST"])
def getPlaySource(request):
    """
    获取播放源
    :param request:
    :return:
    """
    return
