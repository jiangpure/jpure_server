# -*- coding:utf-8 -*-
import time


class LogUtil(object):
    """
    打印Log的工具类
    """
    ARG = ""
    START_TIME = 0
    END_TIME = 0

    def __init__(self):
        super(LogUtil, self).__init__()

    # 储存（是否打印）
    @classmethod
    def i(cls, message, is_print=True):
        if is_print: print(message)
        cls.ARG += (message + "\n")

    # 保存Log日志
    @classmethod
    def saveLog(cls, log_path):
        with open(log_path, "w", encoding="utf-8") as file:
            file.write(cls.ARG)

    # 日志段落开始
    @classmethod
    def startLog(cls, tag="log-start"):
        cls.START_TIME = time.time()
        message = tag.center(20, "=") + "\n"
        print(message)
        cls.ARG += (message)

    # 段落结束
    @classmethod
    def endLog(cls):
        message = "耗时：%0.3f秒" % (time.time() - cls.START_TIME)
        print(message.center(20, "=") + "\n")
        cls.ARG += (message.center(20, "=") + "\n")


if __name__ == "__main__":
    pass
    # LogUtil.startLog()
    # time.sleep(3)
    # LogUtil.i("hehhehhehehehehe")
    # LogUtil.endLog()
    # LogUtil.saveLog(r"C:\Users\Administrator.PC-20180314KCTP\Desktop\ascasc.txt")
