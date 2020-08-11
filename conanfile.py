#!/usr/bin/env python3
# coding=utf-8

import os
import sys
import io
from conans import ConanFile, CMake, tools

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gbk')
# os.system("chcp 65001")


class HelloWorldConan(ConanFile):
    name = "HelloWorld"
    version = "0.0.1"
    license = "This project is licensed under GLWTPL"
    author = "daixian<amano_tooko@qq.com>"
    url = "https://github.com/daixian/conan-helloword-template"
    description = "使用自己的初始模板构建的工程"
    topics = ("opencv", "daixian")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False,
                       "dlog:shared": False,
                       "boost:without_test": True,
                       "poco:enable_data_sqlite": False}
    generators = "cmake"
    exports_sources = "src/*"

    def requirements(self):
        # 通常引用这些个库
        self.requires("boost/1.71.0")
        self.requires("eigen/3.3.7")
        self.requires("poco/[>=1.10.1]@daixian/stable")
        self.requires("dlog/[>=2.5.2]@daixian/stable")
        self.requires("xuexuejson/[>1.1.0]@daixian/stable")

    def _configure_cmake(self):
        '''
        转换python的设置到CMake
        '''
        cmake = CMake(self)
        # 目前没有写导出类,所以实际上不能支持BUILD_SHARED
        cmake.definitions["CVSYSTEM_BUILD_SHARED"] = self.options.shared
        return cmake

    def build(self):
        print("进入了build...")
        cmake = self._configure_cmake()
        cmake.configure(source_folder="src")
        cmake.build()

        # Explicit way:
        # self.run('cmake %s/hello %s'
        #          % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include", src="src")
        self.copy("*.hpp", dst="include", src="src")

        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["HelloWorld"]
        # 附带引用这些库
        # if self.settings.os == "Windows":
        #     self.cpp_info.libs.append("baseclasses")
