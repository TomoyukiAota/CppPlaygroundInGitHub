cmake_minimum_required(VERSION 3.3)
project(CppPlayground CXX)

set( CMAKE_CXX_STANDARD 14 )
set( CMAKE_CXX_STANDARD_REQUIRED  ON )
set( CMAKE_CXX_EXTENSIONS  OFF )

enable_testing()

set_property( GLOBAL  PROPERTY  USE_FOLDERS  ON )

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

add_compile_options(
    "$<$<CXX_COMPILER_ID:MSVC>:/W4>"
    "$<$<CXX_COMPILER_ID:GNU>:-Wall;-Wextra;-Wpedantic>"
    "$<$<CXX_COMPILER_ID:Clang>:-Weverything;-Wno-c++98-compat>"
)

add_subdirectory(src)
add_subdirectory(test)