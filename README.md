# Installations

## Windows

### Conan
* `pacman -S mingw-w64-x86_64-python-conan`

Also do the following once:
 * `conan remote update conancenter --url https://center2.conan.io`


# Build Commands
## Install dependencies:
 * `conan install . --output-folder=build --build=missing`

## Configure:
 * `cd build`
 * `cmake .. -G Ninja -DCMAKE_TOOLCHAIN_FILE=conan_toolchain.cmake -DLV_CONF_INCLUDE_SIMPLE=1`

## Build
 * `cmake --build .`

