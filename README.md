# CppPlayground
Playground for C++.

## Prerequisite
 - Python 3 with `pipenv` installed
 - CMake
 - C++ complier (This will be used as the generator in CMake)
   - e.g. Visual Studio (on Windows) 

## Setup
You need to configure Conan-related settings.
After cloning this repository, issue the following commands:

```
pipenv install
pipenv run conan remote add <REMOTE> https://api.bintray.com/conan/bincrafters/public-conan
```

Replace `<REMOTE>` as you prefer (like `bincrafters-public-conan`). It can be anything as long as it does not already exist in your environment. (See the result of `pipenv run conan remote list` command for existing remotes.)

## Build
Issue the following commands:

```
mkdir build
cd build
pipenv run conan install ..
pipenv run conan build ..
```

After above commands, CMake will generate the target depending on the C++ compiler.

For example, if Visual Studio is used on Windows, `CppPlayground.sln` will be generated.
