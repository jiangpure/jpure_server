## API说明
#### 返回参数：
|字段|类型|说明|备注|
|:-:|:-:|:-:|:-:|
|code|int|状态码|200表示成功，201为失败|
|msg|string|状态码描述||
|data|json|返回数据||


---
#### 初始化
|请求方式|请求地址|
|:-:|:-:|
|POST|HOST/yikan/init|
- ##### 请求参数：
|参数名|是否必须|类型|说明|
|:-:|:-:|:-:|:-:|
|package_name|是|string|包名|
|version_name|是|string|版本名|
|version_code|是|int|版本号|
|app_sign|是|string|app签名|
|ad_ver|是|string|广告版本，渠道标识|
|device_info|是|json|设备信息|
|net_type|是|string|网络类型|
|time|是|string|时间戳|
|sign|是|string|签名值|

###### device_info说明：
|字段|类型|说明|备注|
|:-:|:-:|:-:|:-:|
|imei|string|imei||
|oaid|string|移动安全联盟oaid||
|cpu|string|cpu架构||
|mac|string|mac地址||
|name|string|设备名||
|product|string|产品型号||
|api|string|系统API||
|sys_ver|string|系统版本||
|os|string|系统||
|emulator|boolean|是否模拟器||
|screen|string|设备分辨率||

- ##### 返回示例：
```json
{
  "code": 200,
  "msg": "success",
  "data": {
    "access_token": "agdg2cs71hklacvbjpo9",
    "is_login": false,
    "is_debug": false,
    "is_show_dev_info": true,
    "is_auto_check_update": true,
    "is_ban": false,
    "ext": ""
  },
  "sign": "afh1012h3g87yigf"
}
```

###### data说明：
|字段|类型|说明|备注|
|:-:|:-:|:-:|:-:|
|access_token|string|用户token||
|is_login|boolean|是否开启登录||
|is_debug|boolean|是否开启debug模式||
|is_show_dev_info|boolean|是否显示开发者信息||
|is_auto_check_update|boolean|是否自动检查更新||
|is_ban|boolean|是否禁止进入App||
|ext|string|透传参数|一般为空|


---
#### 检查更新

|请求方式|请求地址|
|:-:|:-:|
|POST|HOST/yikan/check_update|
- ##### 请求参数：
|参数名|是否必须|类型|说明|
|:-:|:-:|:-:|:-:|
|access_token|是|string|包名|
|version_code|是|int|版本号|
|app_sign|是|string|app签名|
|time|是|String|时间戳|
|sign|是|String|签名值|

- ##### 返回示例：
```json
{
  "code": 200,
  "msg": "success",
  "data": {
    "new_version_code": 5,
    "new_version_name": "0.0.5-bate",
    "app_sign": "1",
    "apk_size": 1,
    "apk_md5": "1",
    "pop_config": {
      "tag": "test",
      "width_percent": 0.8,
      "height_percent": 0.5,
      "dim_amount": 0.3,
      "title": "测试",
      "confirm_txt": "确认",
      "cancel_txt": "取消",
      "enforce": false,
      "content": "测试和四十回撕扯hi测试后"
    },
    "new_apk_url": "https://www.baidu.apk",
    "ext": "2"
  },
  "sign": "afh1012h3g87yigf"
}
```

###### data说明：
|字段|类型|说明|备注|
|:-:|:-:|:-:|:-:|
|new_version_code|int|新版本号||
|new_version_name|string|新版本名||
|sign_md5|string|签名的md5||
|apk_md5|string|文件的md5值||
|apk_size|string|文件的大小||
|pop_config|json|弹窗配置||
|new_apk_url|string|新版下载地址||
|ext|string|透传参数|一般为空|

###### pop_config说明：
|字段|类型|说明|备注|
|:-:|:-:|:-:|:-:|
|tag|string|标识||
|width_percent|float|宽占屏幕的比值（0~1）||
|height_percent|float|高占屏幕的比值（0~1）||
|dim_amount|float|阴影深浅值（0~1）||
|title|string|标题||
|confirm_txt|string|确认按钮的字符||
|cancel_txt|string|取消按钮的字符||
|new_apk_url|string|新apk的下载地址||
|ext|string|透传参数|一般为空|
---