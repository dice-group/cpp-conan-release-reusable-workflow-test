cmake_minimum_required(VERSION 3.21)
project(cpp-conan-release-reusable-workflow-test
        VERSION 0.11.4
        DESCRIPTION "For testing how things need to be set up."
        )

add_library(cpp-conan-release-reusable-workflow-test INTERFACE)

target_include_directories(
        cpp-conan-release-reusable-workflow-test
        INTERFACE
        "$<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/src>")

include(cmake/install_interface_library.cmake)
install_interface_library(${PROJECT_NAME} ${PROJECT_NAME} ${PROJECT_NAME} "include")
