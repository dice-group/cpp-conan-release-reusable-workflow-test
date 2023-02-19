import os
import re

from conan.tools.cmake import CMake, cmake_layout

from conan import ConanFile

from conan.tools.files import load, copy


class Recipe(ConanFile):
    name = "cpp-conan-release-reusable-workflow-test"
    version = None

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    exports_sources = "include/*"
    no_copy_source = True

    generators = ("CMakeDeps", "CMakeToolchain")

    def set_version(self):
        if not hasattr(self, 'version') or self.version is None:
            cmake_file = load(self, os.path.join(self.recipe_folder, "CMakeLists.txt"))
            self.version = re.search(r"project\([^)]*VERSION\s+(\d+\.\d+.\d+)[^)]*\)", cmake_file).group(1)

    _cmake = None

    # def layout(self):
    #     cmake_layout(self)

    def package(self):
        copy(self, "*.hpp", self.source_folder, self.package_folder)

    # def package_id(self):
    #     self.info.clear()
