import os
import re

from conan import ConanFile
from conan.tools.cmake import CMake

from conan.tools.files import copy, load, rmdir


class ReusableWorkflowTest(ConanFile):
    author = "DICE Group <info@dice-research.org>"
    settings = "os", "compiler", "build_type", "arch"
    package_type = "header-library"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    exports_sources = "include/*", "CMakeLists.txt", "cmake/*"
    no_copy_source = True

    generators = "CMakeDeps", "CMakeToolchain"

    def set_name(self):
        if not hasattr(self, 'name') or self.version is None:
            cmake_file = load(self, os.path.join(self.recipe_folder, "CMakeLists.txt"))
            self.name = re.search(r"project\(\s*([a-z\-]+)\s+VERSION", cmake_file).group(1)

    def set_version(self):
        if not hasattr(self, 'version') or self.version is None:
            cmake_file = load(self, os.path.join(self.recipe_folder, "CMakeLists.txt"))
            self.version = re.search(r"project\([^)]*VERSION\s+(\d+\.\d+.\d+)[^)]*\)", cmake_file).group(1)

    def package(self):
        cmake = CMake(self)
        cmake.configure(variables={})
        cmake.install()

        for dir in "lib", "res", "share":
            rmdir(self, os.path.join(self.package_folder, dir))

    def package_info(self):
        self.cpp_info.bindirs = []
        self.cpp_info.libdirs = []

        self.cpp_info.set_property("cmake_find_mode", "both")
        self.cpp_info.set_property("cmake_target_name", f"{self.name}::{self.name}")
        self.cpp_info.set_property("cmake_file_name", self.name)
