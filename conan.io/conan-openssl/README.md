[![Build Status](https://travis-ci.org/leapmotion/conan-openssl.svg?branch=master)](https://travis-ci.org/leapmotion/conan-openssl)

[![Join the chat at https://gitter.im/leapmotion/conan-openssl](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/leapmotion/conan-openssl?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

# conan-openssl

[Conan.io](https://conan.io) package for OpenSSL library

The packages generated with this **conanfile** can be found in [conan.io](https://conan.io/source/OpenSSL/1.0.2j/leapmotion/stable1.2.8/leapmotion/stable).

## Build packages

Download conan client from [Conan.io](https://conan.io) and run:

    $ python build.py
    
## Upload packages to server

    $ conan upload OpenSSL/1.0.2j@leapmotion/stable --all
    
## Reuse the packages

### Basic setup

    $ conan install OpenSSL/1.0.2j@leapmotion/stable
    
### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*
    
    [requires]
    OpenSSL/1.0.2j@leapmotion/stable

    [options]
    OpenSSL:shared=true # false
    # Take a look for all available options in conanfile.py
    
    [generators]
    txt
    cmake

Complete the installation of requirements for your project running:</small></span>

    conan install .

Project setup installs the library (and all his dependencies) and generates the files *conanbuildinfo.txt* and *conanbuildinfo.cmake* with all the paths and variables that you need to link with your dependencies.
