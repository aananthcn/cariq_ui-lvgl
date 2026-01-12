# Clone this repo
 * `git clone https://github.com/aananthcn/cariq_ui-lvgl.git`
 * `git submodule update --init --recursive`

<br>

# Build Commands
## Install dependencies:
 * `conan install . --output-folder=build --build=missing`

## Configure:
##### Option A
 * `cd build`
 * `cmake .. -G Ninja -DCMAKE_TOOLCHAIN_FILE=conan_toolchain.cmake -DLV_CONF_INCLUDE_SIMPLE=1`
##### Option B
 * `cmake --preset conan-release`


## Build
##### Option A
 * `cmake --build .`
##### Option B
 * `cmake --build --preset conan-release`


<br>

# Installations

## Windows

### Conan
* `pacman -S mingw-w64-x86_64-python-conan`

Also do the following once:
 * `conan remote update conancenter --url https://center2.conan.io`

### MinGW64

`vi $(conan profile path default)`

Then add the following inside it
```
[settings]
os=Windows
arch=x86_64
compiler=gcc
compiler.version=15
compiler.libcxx=libstdc++11
compiler.cppstd=gnu17
build_type=Release

[conf]
# 1. Force the exact MinGW executables (Prevents picking up MSVC)
tools.build:compiler_executables={'c': 'C:/msys64/mingw64/bin/gcc.exe', 'cpp': 'C:/msys64/mingw64/bin/g++.exe'}

# 2. Relax GCC 15 strictness (Fixes the _stati64 / incompatible types errors)
tools.build:cflags=["-Wno-error=incompatible-pointer-types", "-fpermissive"]
tools.build:cxxflags=["-fpermissive"]

[buildenv]
# 3. Ensure MinGW is at the front of the PATH during builds
PATH+=(path)C:/msys64/mingw64/bin
```



## MacOS
Follow these steps
 * If xcode is not installed
   * `xcode-select --install`
 * If Homebrew is not installed
   * `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
 * Install packages required for this project
   * `brew install conan cmake ninja sdl2`
 * Update conan center
   * `conan remote update conancenter --url https://center2.conan.io`
 * Create or Update default profiel
   * `conan profile detect --force`
   * And it should contain the following
     ```
	 [settings]
	 arch=armv8
	 build_type=Release
	 compiler=apple-clang
	 compiler.cppstd=gnu17
	 compiler.libcxx=libc++
	 compiler.version=17
	 os=Macos
	 ```







