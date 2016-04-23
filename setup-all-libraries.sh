#!/bin/bash

INSTALL_ROOT=/c/dev/Libraries-x64_vc15
./setup-library.sh http://downloads.sourceforge.net/project/boost/boost/1.60.0/boost_1_60_0.7z 1.60.0 ${INSTALL_ROOT} -s "boost_1_60_0" -o "boost_1_60_0"
./setup-library.sh git@github.com:madler/zlib.git 1.2.8 ${INSTALL_ROOT}
./setup-library.sh git@github.com:openssl/openssl.git 1.0.2g ${INSTALL_ROOT}
./setup-library.sh git@github.com:curl/curl.git 7.48.0 ${INSTALL_ROOT}
./setup-library.sh http://download.icu-project.org/files/icu4c/57.1/icu4c-57_1-src.zip 57.1 ${INSTALL_ROOT} -s "icu" -o "icu-57.1" -n "icu"
./setup-library.sh git://code.qt.io/qt/qt5.git 5.6.0 ${INSTALL_ROOT} -o "qt-5.6.0"
./setup-library.sh git@github.com:google/flatbuffers.git 1.3.0 ${INSTALL_ROOT}
./setup-library.sh git@github.com:google/protobuf.git 3.0.0-beta-2 ${INSTALL_ROOT}
./setup-library.sh git@github.com:leapmotion/leapserial.git 0.3.2 ${INSTALL_ROOT}
./setup-library.sh git@github.com:crossroads-io/libxs.git 1.2.0 ${INSTALL_ROOT}
./setup-library.sh git@github.com:dcnieho/FreeGLUT.git 3.0.0 ${INSTALL_ROOT} -b FG_3_0_0
./setup-library.sh git@github.com:zaphoyd/websocketpp.git 0.7.0 ${INSTALL_ROOT} -b0.7.0
#./setup-library.sh https://ftp.mozilla.org/pub/security/nss/releases/NSS_3_23_RTM/src/nss-3.23-with-nspr-4.12.tar.gz 3.23 ${INSTALL_ROOT} -s "nss-3.23" -o "nss-3.23" -n "nss"
./setup-library.sh https://www.libsdl.org/release/SDL2-devel-2.0.4-VC.zip 2.0.4 ${INSTALL_ROOT}
./setup-library.sh git@github.com:nigels-com/glew.git 1.13.0 ${INSTALL_ROOT}
./setup-library.sh http://downloads.sourceforge.net/freeimage/FreeImage3170.zip 3.17.0 ${INSTALL_ROOT}
./setup-library.sh https://sourceforge.net/projects/anttweakbar/files/latest/download?source=dlp 1.16 ${INSTALL_ROOT}
./setup-library.sh git@github.com:bulletphysics/bullet3.git 2.83.7 ${INSTALL_ROOT}
