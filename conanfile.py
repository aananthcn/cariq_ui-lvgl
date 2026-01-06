from conan import ConanFile
from conan.tools.cmake import cmake_layout
import os

class CarIQUIRecipe(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps", "CMakeToolchain"

    def requirements(self):
        self.requires("lvgl/9.1.0")
        self.requires("sdl/2.30.1")

    def layout(self):
        cmake_layout(self)

    def generate(self):
        # self.recipe_folder is the absolute path to your App's root
        header_path = os.path.join(self.recipe_folder, "src", "lv_conf.h")
        # Ensure we use forward slashes for the conf string to avoid escape char issues
        header_path = header_path.replace("\\", "/")
        self.conf_info.define("user.lvgl:config_path", header_path)