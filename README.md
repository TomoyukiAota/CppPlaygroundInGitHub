# CppPlayground
Playground for C++

## Prerequisite
 - Python 3 with `pipenv` installed
 - CMake
 - C++ complier (This will be used as the generator in CMake)
   - e.g. Visual Studio (on Windows) 

## How to setup
After cloning this repository, issue the following commands:

```
pipenv install
mkdir build
cd build
pipenv run conan install ..
pipenv run conan build ..
```

After above commands, CMake will generate the target depending on the C++ compiler.

For example, if Visual Studio is used on Windows, `CppPlayground.sln` will be generated.
