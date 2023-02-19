cmake_minimum_required(VERSION 3.15)
project(PackageTest CXX)

find_package(cpp-conan-release-reusable-workflow-test REQUIRED)

add_executable(example example.cpp)

target_link_libraries(example PUBLIC
        cpp-conan-release-reusable-workflow-test::cpp-conan-release-reusable-workflow-test)

set_target_properties(
        example PROPERTIES
        CXX_STANDARD 20
        CXX_STANDARD_REQUIRED ON
        CXX_EXTENSIONS OFF
)
