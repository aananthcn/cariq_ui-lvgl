cmake_minimum_required(VERSION 3.15)
project(CarIQ-ui LANGUAGES C CXX)

# 1. LVGL configuration MUST be set before adding the subdirectory
# This tells LVGL to use your custom header instead of its template
set(LV_CONF_PATH "${CMAKE_SOURCE_DIR}/src/lv_conf.h" CACHE STRING "" FORCE)
set(LV_BUILD_CONF_PATH "${CMAKE_SOURCE_DIR}/src/lv_conf.h" CACHE STRING "" FORCE)
set(LV_CONF_SKIP OFF CACHE BOOL "" FORCE)

# 2. Add the LVGL source directory (the submodule)
add_subdirectory(libs/lvgl)

# 3. Find packages provided by Conan
find_package(SDL2 REQUIRED)

add_executable(${PROJECT_NAME} 
    src/main.cpp
)

# 5. Application specific includes and definitions
target_include_directories(${PROJECT_NAME} PRIVATE src)
target_compile_definitions(${PROJECT_NAME} PRIVATE 
    LV_CONF_INCLUDE_SIMPLE=1
	SDL_MAIN_HANDLED
)

# 6. Link the libraries
# We link against 'lvgl' (the target name defined inside the submodule)
target_link_libraries(${PROJECT_NAME} PRIVATE 
    lvgl::lvgl
    SDL2::SDL2
)

# Add this to bridge the gap between the LVGL submodule and your Conan SDL2 package
target_link_libraries(lvgl PUBLIC SDL2::SDL2)