#!/usr/bin/env python3
# coding=utf-8

import os

from conans import ConanFile, CMake, tools


class CVSystemTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    default_options = {"dlog:shared": False,
                       "opencv:shared": True,
                       "boost:without_test": True,
                       "poco:enable_data_sqlite": False}

    def requirements(self):
        """作为一个test_package这里需要包含所有的依赖"""
        self.requires("boost/1.71.0")
        self.requires("eigen/3.3.7")
        self.requires("poco/[>=1.10.1]@daixian/stable")
        self.requires("dlog/[>=2.5.2]@daixian/stable")
        self.requires("xuexuejson/[>1.1.0]@daixian/stable")

    def build_requirements(self):
        self.build_requires("gtest/1.8.1@bincrafters/stable")

    def build(self):
        cmake = CMake(self)
        # Current dir is "test_package/build/<build_id>" and CMakeLists.txt is
        # in "test_package"
        cmake.configure()
        cmake.build()

    def imports(self):
        self.copy("*.dll", dst="bin", src="bin")
        self.copy("*.dylib*", dst="bin", src="lib")
        self.copy('*.so*', dst='bin', src='lib')

    def test(self):
        if not tools.cross_building(self.settings):
            os.chdir("bin")
            self.run('.%stest.out --gtest_output="xml:gtest_report.xml"' % os.sep)
