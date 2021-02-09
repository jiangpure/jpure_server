# -*- coding:utf-8 -*-
import os
import re
import shutil
import hashlib


class FileUtils(object):
    UNIT_B = "B"
    UNIT_KB = "K"
    UNIT_MB = "M"
    UNIT_GB = "G"
    REGULAR_TIME = "time"
    REGULAR_NAME = "name"
    REGULAR_SIZE = "size"
    TYPE_DIR = "type_dir"
    TYPE_FILE = "type_file"
    TYPE_BOTH = "type_both"

    # 判断文件是否存在
    @classmethod
    def file_exist(cls, file_path):
        return os.path.exists(os.path.abspath(file_path))

    # 文件路径获取文件对象
    @classmethod
    def file(cls, file_path):
        if cls.file_exist(file_path):
            return open(file_path, encoding="utf-8")

    # 文件路径获取文件对象
    @classmethod
    def absolute_path(cls, file_path):
        return os.path.abspath(file_path)

    # 判断是文件还是文件夹,文件返回True,文件夹返回False,不存在返回None
    @classmethod
    def file_or_dir(cls, file_path):
        if cls.file_exist(file_path):
            return os.path.isfile(os.path.abspath(file_path))

    # 创建空目录
    @classmethod
    def create_dir(cls, dir_path):
        if not cls.file_exist(dir_path):
            os.makedirs(dir_path)
            return True
        else:
            return True

    # 创建文件
    @classmethod
    def create_file(cls, file_path):
        try:
            with open(file_path, "a+"):
                return True
        except Exception as e:
            print(e)
            return False

    @classmethod
    def writeFile(cls, file_path, content, clear=False):
        try:
            with open(file_path, "a+") as f:
                if clear:
                    f.truncate()
                f.write(content)
                return True
        except Exception as e:
            print(e)
            return False

    @classmethod
    def clearFile(cls, file_path):
        try:
            with open(file_path, "a+") as f:
                f.truncate()
                return True
        except Exception as e:
            print(e)
            return False


    # 删除文件或者文件夹
    @classmethod
    def del_file(cls, file_path):
        if cls.file_exist(file_path):
            print(file_path)
            if cls.file_or_dir(file_path):
                os.remove(file_path)
            else:
                shutil.rmtree(file_path)
            return True

    # 重命名文件或者文件夹
    @classmethod
    def rename(cls, file_path, new_name):
        if cls.file_exist(file_path):
            os.renames(file_path, os.path.dirname(file_path).join(new_name))
            return True

    # 复制文件或者文件夹
    @classmethod
    def copy_file(cls, old_path, new_path, is_write=False):
        print("f:%s--s:%s" % (old_path, new_path))
        if cls.file_exist(old_path) and cls.file_exist(new_path) and is_write:
            cls.del_file(new_path)
        try:
            if cls.file_or_dir(old_path):
                shutil.copy(old_path, new_path)
            else:
                shutil.copytree(old_path, new_path)
            return True
        except FileNotFoundError as a:
            print(a)
        return False

    # 移动文件或者文件夹
    @classmethod
    def move_file(cls, old_path, new_path, is_write=False):
        if cls.file_exist(old_path) and cls.file_exist(new_path) and is_write:
            cls.del_file(new_path)
        try:
            shutil.move(old_path, new_path)
        except FileExistsError as a:
            print(a)
            return False
        return True

    # 合并两个目录
    @classmethod
    def merge_dir(cls, first_dir, second_dir, is_write=False, is_delete=False):
        print("f:%s--s:%s" % (first_dir, second_dir))
        try:
            first_lists = os.listdir(first_dir)
            for files in first_lists:
                print(files)
                if is_write:
                    cls.del_file(os.path.join(second_dir, files))
                    cls.copy_file(os.path.join(first_dir, files), os.path.join(second_dir, files), is_write)
            if is_delete:
                cls.del_file(first_dir)
            return True
        except Exception as a:
            print(a)
            return False

    # 删除另一个文件夹中的同名文件
    @classmethod
    def diff(cls, first_dir, second_dir):
        if not cls.file_exist(first_dir) or not cls.file_exist(second_dir):
            return False
        for files in os.listdir(first_dir):
            print(files)
            new_files = os.path.join(second_dir, files)
            if cls.file_exist(new_files):
                if cls.file_or_dir(files):
                    cls.diff(os.path.join(first_dir, files), new_files)
                else:
                    cls.del_file(new_files)

    # 获取文件后缀
    @classmethod
    def get_suffix(cls, file_path):
        return os.path.splitext(file_path)[1]

    # 获取文件名(suffix:有无后缀)
    @classmethod
    def get_filename(cls, file_path, suffix=True):
        if suffix:
            return os.path.basename(file_path)
        return os.path.splitext(os.path.basename(file_path))[0]

    # 获取文件内容并返回为字符串
    @classmethod
    def get_filecontent(cls, file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()

    # 获取文件大小,单位为字节
    @classmethod
    def get_filesize(cls, file_path, unit):
        size = os.path.getsize(file_path)
        if unit == cls.UNIT_B:
            return size
        elif unit == cls.UNIT_KB:
            return size / 1024.0
        elif unit == cls.UNIT_MB:
            return size / 1024.0 ** 2
        elif unit == cls.UNIT_GB:
            return size / 1024.0 ** 3

    # 获取目录下的所有文件
    @classmethod
    def get_file(cls, file_path, regex, recursive=False):
        if recursive:
            cls.get_child(file_path, regex)
        else:
            return cls.get_child(file_path, regex)

    # 获取目录下的所有文件
    @classmethod
    def get_all_child(cls, file_path, regex, file_list=None):
        if file_list is None:
            file_list = []
        if cls.file_exist(file_path):
            files = os.listdir(file_path)
            for file in files:
                temp_path = os.path.join(file_path, file)
                if cls.file_or_dir(temp_path) and regex is cls.TYPE_FILE:
                    file_list.append(temp_path)
                elif not cls.file_or_dir(temp_path):
                    if regex is cls.TYPE_DIR:
                        file_list.append(temp_path)
                    cls.get_all_child(temp_path, regex, file_list)
            return file_list

    # 获取目录下文件/文件夹(不包括子目录)
    @classmethod
    def get_child(cls, file_path, regex):
        if cls.file_exist(file_path):
            files = os.listdir(file_path)
            if regex is cls.TYPE_FILE:
                return [os.path.join(file_path, file) for file in files if cls.file_or_dir(file)]
            elif regex is cls.TYPE_DIR:
                return [os.path.join(file_path, file) for file in files if not cls.file_or_dir(file)]
            else:
                return [os.path.join(file_path, file) for file in files]

    # 文件排序
    @classmethod
    def sort_file(cls, dir_path, regular):
        file_list = os.listdir(dir_path)
        if regular is cls.REGULAR_NAME:
            return sorted(file_list, key=lambda x: os.path.basename(os.path.join(dir_path, x)))
        elif regular is cls.REGULAR_SIZE:
            return sorted(file_list, key=lambda x: os.path.getsize(os.path.join(dir_path, x)))
        elif regular is cls.REGULAR_TIME:
            return sorted(file_list, key=lambda x: os.path.getmtime(os.path.join(dir_path, x)))

    # 获取父目录的绝对路径
    @classmethod
    def get_parentdir(cls, file_path):
        return os.path.abspath(os.path.dirname(file_path))

    # 判断两个路径是否指向同一文件夹/文件
    @classmethod
    def check_same(cls, first_file, second_file):
        return os.path.samefile(first_file, second_file)

    # 判断文件内容是否相同
    @classmethod
    def check_samefile(cls, first_file, second_file):
        with open(first_file, "r", encoding="utf-8") as file:
            content = file.read()

    # 替换文件内容(支持正则式)
    @classmethod
    def replace(cls, file_path, old_str, new_str):
        with open(file_path, "r+", encoding="UTF-8") as file:
            content = ""
            for line in file.readlines():  content += line
            re.sub(old_str, new_str, content)
            file.write(content)

    # 获取文件MD5
    @classmethod
    def get_md5(cls, file_path):
        return hashlib.md5(open(file_path, 'rb').read()).hexdigest()


if __name__ == "__main__":
    pass
    # result = FileUtils.get_all_child(
    #     r"C:\Users\Administrator.PC-20180314KCTP\Desktop\BlankTool\BlankToolv0.2\package\app-release",
    #     regex=FileUtils.TYPE_DIR)
    # print(len(result))
