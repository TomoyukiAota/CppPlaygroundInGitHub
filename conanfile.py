from conans import ConanFile, CMake


class CppPlayground(ConanFile):
    name = "CppPlayground"
    version = "0.01"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "Playground for C++"

    settings = {
                   'compiler': None,
                   'arch': ['x86_64'],
                   'build_type': ['Release', 'Debug'],
                   'os': None
               }
    options = {"shared": [True, False]}
    default_options = "shared=True"
    short_paths = True
    generators = "cmake"
    build_policy = 'missing'
    exports_sources = 'CMakeLists.txt', 'cmake*', 'include*', 'src*', 'test*', 'tools*'

    @property
    def _is_dev(self):
        try:
            return self.develop
        except AttributeError:
            try:
                return self.scope.dev
            except AttributeError:
                return False

    def configure(self):
        if self._is_dev:
            self.requires('gtest/1.8.0@bincrafters/stable', 'private')
            self.options['gtest'].shared = False    # gtest has some unusual behavior when included statically
        if self.settings.compiler == 'Visual Studio':
            if self.settings.build_type == 'Debug':
                self.options['gtest'].include_pdbs = True

    def build(self):
        cmake = CMake(self)

        cmake_cxx_flags = list()
        if self.settings.compiler == 'Visual Studio':
            cmake_cxx_flags += ['/D_SILENCE_TR1_NAMESPACE_DEPRECATION_WARNING']     # Suppress C4996 warning from gtest compiled with VS2017
            cmake_cxx_flags += ['/EHsc']                                            # Resolve C4530 warning

        cmake_cxx_flags = ' '.join(cmake_cxx_flags)

        gen_extra_args = list()
        gen_extra_args += ['-DBUILD_SHARED_LIBS=ON'] if self.options.shared else ['-DBUILD_SHARED_LIBS=OFF']
        gen_extra_args += [f'-DCMAKE_CXX_FLAGS=\"{cmake_cxx_flags}\"']
        gen_extra_args = ' '.join(gen_extra_args)
        self.run('cmake "{:s}" {:s} {:s}'.format(self.source_folder, cmake.command_line, gen_extra_args))

        build_extra_args = list()
        build_extra_args += ['-- -j -k'] if self.settings.compiler in ['gcc', 'clang'] else ['']
        build_extra_args = ' '.join(build_extra_args)
        self.run('cmake --build . {:s} {:s}'.format(cmake.build_config, build_extra_args))

    def package(self):
        self.copy("*.h", dst="include", src="src")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)
        # copy debug symbols
        if self.settings.compiler == 'Visual Studio' and self.settings.build_type == 'Debug':
            self.copy(pattern='*.pdb', dst='bin', src='.', keep_path=False)

    def package_info(self):
        self.cpp_info.libs = [self.name]
