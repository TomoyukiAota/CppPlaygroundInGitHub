project(HelloTest)
FILE(GLOB srcfiles *cpp)
FILE(GLOB headerfiles *h)
add_executable(HelloTest ${srcfiles} ${headerfiles})

target_link_libraries(HelloTest
    PRIVATE CONAN_PKG::gtest
    PRIVATE Hello
)

target_include_directories(HelloTest
    PRIVATE "${CONAN_INCLUDE_DIRS_MICROSOFT-GSL}"
    PRIVATE "${Hello_SOURCE_DIR}"
)

add_test(NAME HelloTest COMMAND HelloTest)
