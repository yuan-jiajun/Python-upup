# coding:utf-8

import os


def walk(dirname):
    '''
    以绝对路径，用列表输出指定目录下的所有文件，以及子文件夹下的文件。
    '''
    names = []
    for name in os.listdir(dirname):
        # os.listdir() Return a list containing the names of the entries in the directory given by path.

        path = os.path.join(dirname, name)
        # os.path.join() Join one or more path components intelligently

        if os.path.isfile(path):
            # os.path.isfile() Return True if path is an existing regular file.判断是否为文件
            names.append(path)
        else:
            names.extend(walk(path))  # list.extend()

    return names  # 返回指定文件下所有文件的列表


def find_suffix_file(dirname, suffix):
    '''
    以列表输出指定后缀名的文件。
    '''
    target_files = []

    names = walk(dirname)  # 调用自定义函数walk()

    for name in names:

        if name.endswith(suffix):
            target_files.append(name)

    return target_files  # 返回目标文件列表


def call_cmd(cmd):
    '''
    windows下文件MD5等校验：(LINUX 下，使用md5sum命令)

    certutil -hashfile 路径/file.exe MD5

    certutil -hashfile 路径/file.exe SHA1

    certutil -hashfile 路径/file.exe SHA256

    '''

    fp = os.popen(cmd)  # Python下调用系统命令行，返回一个文件对象
    # Open a pipe to or from command cmd.
    # The return value is an open file object connected to the pipe,
    # which can be read or written depending on whether mode is 'r' (default) or 'w'.

    result = fp.read()  # 读取命令行执行的返回的内容

    state = fp.close()  # 关闭文件对象

    assert state is None  # 断言文件对象是否关闭

    return result  # 返回命令行计算的结果


def compute_md5(filename):
    '''
    compute the MD5 value of the file
    '''

    # 构建命令行 命令

    cmd = 'certutil -hashfile "' + filename + '" MD5'

    # 注意：命令构建时，由于文件路径中含有空格，命令行执行时会将空格识别为分隔符，
    # 误识别为多个参数，从而报错 " CertUtil: 参数太多 "。
    # 所以要将文件路径包含在双引号""内。

    result = call_cmd(cmd)  # 调用CMD，计算MD5值

    file_md5 = tuple(result.split('\n'))[1]  # 解析读取的内容，

    return file_md5  # 返回文件的MD5值


def check_file(dirname, suffix):
    d = {}  # 创建空字典。将md5_value作为key, file 作为value.

    target_files = find_suffix_file(dirname, suffix)

    for file in target_files:

        md5_value = compute_md5(file)  # 计算md5_value

        if md5_value in d:  # 

            d[md5_value].append(file)  # 以列表的形式收集相同MD5值的file
        else:
            d[md5_value] = [file]

    for md5_value, file in d.items():

        if len(file) > 1:  # 如果大于1，说明很可能有不同文件名的重复文件。

            print(file)  # 此处file是收集重复文件的列表


if __name__ == '__main__':
    # 注：指定目录下，文件路径中含有空格时会报错 AssertionError

    dirname = r'F:\notes\paper-read'  # 注意 Windows下路径的写法

    suffix = '.pdf'

    check_file(dirname, suffix)
