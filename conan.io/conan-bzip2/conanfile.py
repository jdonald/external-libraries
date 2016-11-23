from conans import ConanFile
import os, shutil
from conans.tools import download, unzip, replace_in_file, check_md5
from conans import CMake


class Bzip2Conan(ConanFile):
    name = "bzip2"
    version = "1.0.6"
    branch = "master"
    ZIP_FOLDER_NAME = "bzip2-%s" % version
    generators = "cmake"
    settings =  "os", "compiler", "arch", "build_type"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = "shared=False", "fPIC=True"
    exports = ["CMakeLists.txt"]
    url="http://github.com/lasote/conan-bzip2"
    license="BSD-style license"

    def config_options(self):
        try: # Try catch can be removed when conan 0.8 is released
            del self.settings.compiler.libcxx
        except: 
            pass        

    def source(self):
        zip_name = "bzip2-%s.tar.gz" % self.version
        download("http://www.bzip.org/%s/%s" % (self.version, zip_name), zip_name)
        check_md5(zip_name, "00b516f4704d4a7cb50a1d97e6e8e15b")
        unzip(zip_name)
        
        os.unlink(zip_name)

    def build(self):
	if self.settings.compiler == "Visual Studio" and self.settings.build_type == "Debug":
	    if not str(self.settings.compiler.runtime).endswith("d"):
	        self.settings.compiler.runtime = str(self.settings.compiler.runtime) + "d"

        shutil.move("CMakeLists.txt", "%s/CMakeLists.txt" % self.ZIP_FOLDER_NAME)
        cmake = CMake(self.settings)

        self.run("cd %s &&  mkdir _build" % self.ZIP_FOLDER_NAME)
        cd_build = "cd %s/_build" % self.ZIP_FOLDER_NAME
        shared = "-DBUILD_SHARED_LIBS=ON" if self.options.shared else ""
        fpic = "-DFPIC=ON" if self.options.fPIC else ""
        self.run('%s && cmake .. %s %s %s' % (cd_build, cmake.command_line, shared, fpic))
        self.run("%s && cmake --build . %s" % (cd_build, cmake.build_config))

    def package(self):
        # Copying zlib.h, zutil.h, zconf.h
        self.copy("*.h", "include", "%s" % (self.ZIP_FOLDER_NAME), keep_path=False)
        self.copy("*bzip2", dst="bin", src=self.ZIP_FOLDER_NAME, keep_path=False)
        self.copy(pattern="*.so*", dst="lib", src=self.ZIP_FOLDER_NAME, keep_path=False)
        self.copy(pattern="*.a", dst="lib", src="%s/_build" % self.ZIP_FOLDER_NAME, keep_path=False)
        self.copy(pattern="*.lib", dst="lib", src="%s/_build" % self.ZIP_FOLDER_NAME, keep_path=False)
        self.copy(pattern="*.dll", dst="bin", src="%s/_build" % self.ZIP_FOLDER_NAME, keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ['bz2']
