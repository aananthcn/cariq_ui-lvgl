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


# Build Commands
## Install dependencies:
 * `conan install . --output-folder=build --build=missing`

## Configure:
 * `cd build`
 * `cmake .. -G Ninja -DCMAKE_TOOLCHAIN_FILE=conan_toolchain.cmake -DLV_CONF_INCLUDE_SIMPLE=1`

## Build
 * `cmake --build .`

