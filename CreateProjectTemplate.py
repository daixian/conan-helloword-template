#!/usr/bin/env python3
# coding=utf-8

import os
import sys
import io
import getopt

class ReplaceNameProc:
    '''用于给这个项目工程改名'''
    # 类变量
    defaultName = 'HelloWorld'

    def __init__(self, dirPath: str, projectName: str):
        # 下面为Person对象增加2个实例变量
        self.dirPath = dirPath
        self.projectName = projectName

    def Replace(self,):
        '''执行所有位置的替换'''
        # 下面这些文件都是要替换名字的
        self.ReplaceOneFile(os.path.join(self.dirPath, "CMakeLists.txt"))
        self.ReplaceOneFile(os.path.join(self.dirPath, "conanfile.py"))
        self.ReplaceOneFile(os.path.join(
            self.dirPath, "test_package", "conanfile.py"))
        self.ReplaceOneFile(os.path.join(
            self.dirPath, "test_package", "CMakeLists.txt"))
        self.ReplaceOneFile(os.path.join(
            self.dirPath, "src", "CMakeLists.txt"))
        self.ReplaceOneFile(os.path.join(
            self.dirPath, "src", "HelloWorld", "CMakeLists.txt"))

        # 修改文件夹的名字
        os.renames(os.path.join(self.dirPath, "src", "HelloWorld"),
                   os.path.join(self.dirPath, "src", self.projectName),
                   )

    def ReplaceOneFile(self, filePath: str):
        '''执行某一个文件里的替换'''
        f1 = open(filePath, "r", encoding='utf-8')
        content = f1.read()
        f1.close()

        conRep = content.replace(self.defaultName, self.projectName)
        conRep = conRep.replace(self.defaultName.upper(),
                                self.projectName.upper())
        with open(filePath, "w", encoding='utf-8') as f2:
            f2.write(conRep)


def main(argv):
    try:
        # http://www.runoob.com/python/python-command-line-arguments.html?tdsourcetag=s_pcqq_aiomsg
        # 返回值由两个元素组成：第一个是（选项，值）对的列表;第二个是剥离选项列表后留下的程序参数列表（这是第一个参数的尾部切片）。
        # 返回的每个选项和值对都有选项作为其第一个元素，前缀为连字符（例如，' -  x'），
        # 选项参数作为其第二个元素，如果选项没有参数，则为空字符串。选项以与查找顺序相同的顺序出现在列表中，从而允许多次出现。多头和空头选择可能是混合的。
        opts, args = getopt.getopt(
            argv, "hn:t:d:", ["help", "name=", "target=", "dir="])
    except getopt.GetoptError:
        print("参数解析错误!")
        sys.exit(2)

    # 先只实现名字
    name = "unnamed"
    # 目标这里先不实现
    target = "windows"
    # 要执行替换的文件夹目录
    abs_file = __file__
    # print("abs path is %s" % (__file__))
    abs_dir = abs_file[:abs_file.rfind("\\")]   # windows下用\\分隔路径，linux下用/分隔路径

    # 所有的选项部分
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print("--name -n 要设置的库的名字")
            sys.exit()
        elif opt in ("-n", "--name"):
            name = arg
        elif opt in ("-t", "--target"):
            target = arg
        elif opt in ("-d", "--dir"):
            abs_dir = arg

    print("传入的项目名称:" + name)

    # 所有的参数部分
    for arg in args:
        pass

    proc = ReplaceNameProc(abs_dir, name)
    proc.Replace()


if __name__ == "__main__":
    main(sys.argv[1:])