project(Hello)
FILE(GLOB srcfiles *cpp)
FILE(GLOB headerfiles *h)
add_library(Hello STATIC ${srcfiles} ${headerfiles})
