cmake_minimum_required(VERSION 3.15)
project(CarIQ-ui LANGUAGES C CXX)

# Find packages provided by Conan
find_package(lvgl REQUIRED)
find_package(SDL2 REQUIRED)

add_executable(${PROJECT_NAME} 
    src/main.cpp
)

# 1. Tell LVGL to look for "lv_conf.h" without a path
# 2. Add 'src' to include path so #include "lv_conf.h" works
target_compile_definitions(${PROJECT_NAME} PRIVATE LV_CONF_INCLUDE_SIMPLE=1)
target_include_directories(${PROJECT_NAME} PRIVATE src)

# Link the libraries
target_link_libraries(${PROJECT_NAME} PRIVATE lvgl::lvgl SDL2::SDL2)