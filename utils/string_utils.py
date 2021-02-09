# -*- coding:utf-8 -*-
import base64
import hashlib
from urllib.parse import quote, unquote, urlencode


class StringUtils(object):

    # 检查字符串是否为空
    @classmethod
    def empty(cls, str):
        return str is None or len(str.strip()) == 0

    # 首字母转大写
    @classmethod
    def capitalize_firstletter(cls, str):
        if StringUtils.empty(str):
            return str
        return str[0].upper() + str[1:]

    # url utf-8编码
    @classmethod
    def utf8_encode(cls, str, default=""):
        if not StringUtils.empty(str):
            return quote(str, encoding="utf-8")
        return default

    # url utf-8解码
    @classmethod
    def utf8_decode(cls, str, default=""):
        if not StringUtils.empty(str):
            return unquote(str, encoding="utf-8")
        return default

    # base64 utf-8编码
    @classmethod
    def base64_encode(cls, str, default=""):
        if not StringUtils.empty(str):
            return base64.b64encode(str)
        return default

    # base64 utf-8解码
    @classmethod
    def base64_decode(cls, str, default=""):
        if not StringUtils.empty(str):
            return base64.b64decode(str)
        return default

    # 获取字符串的md5
    @classmethod
    def md5(cls, str):
        return hashlib.md5(str).hexdigest()

    # 获取字符串的sha1
    @classmethod
    def sha1(cls, str):
        return hashlib.sha1(str).hexdigest()

if __name__ =="__main__":
    pass
    # content = FileUtils.get_filecontent(r"C:\Users\Administrator.PC-20180314KCTP\Desktop\origin_source.txt")
    # result = StringUtils.base64_decode(StringUtils.base64_decode(content))
    # FileUtils.writeFile(r"C:\Users\Administrator.PC-20180314KCTP\Desktop\新建文本文档1.txt", result.decode())
