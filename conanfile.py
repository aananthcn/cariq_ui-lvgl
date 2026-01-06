from conan import ConanFile
from conan.tools.cmake import CMake, cmake_layout

class CarIQUIRecipe(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps", "CMakeToolchain"

    def requirements(self):
        # SDL is still handled by Conan
        self.requires("sdl/2.30.1")

    def layout(self):
        cmake_layout(self)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()