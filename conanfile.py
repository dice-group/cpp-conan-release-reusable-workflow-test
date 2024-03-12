import os
import re

from conan import ConanFile
from conan.tools.cmake import CMake

from conan.tools.files import load, rmdir, copy


class ReusableWorkflowTest(ConanFile):
    author = "DICE Group <info@dice-research.org>"
    settings = "os", "compiler", "build_type", "arch"
    package_type = "header-library"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    exports_sources = "include/*"
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
        cmake.configure()
        copy(self, "*.hpp", self.source_folder, self.package_folder)
