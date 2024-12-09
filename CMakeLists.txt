# Copyright 2024 Lawrence Livermore National Security, LLC
# See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: BSD-3-Clause

cmake_minimum_required(VERSION 3.20)

project(TippecanoePythonDistributions NONE)

set(default_build_type "Release")
if(NOT CMAKE_BUILD_TYPE AND NOT CMAKE_CONFIGURATION_TYPES)
  message(STATUS "Setting build type to '${default_build_type}' as none was specified.")
  set(CMAKE_BUILD_TYPE "${default_build_type}" CACHE
      STRING "Choose the type of build." FORCE)
  set_property(CACHE CMAKE_BUILD_TYPE PROPERTY STRINGS
    "Debug" "Release" "MinSizeRel" "RelWithDebInfo")
endif()

enable_language(CXX)
include(ExternalProject)

include(tippecanoe_version.cmake)

set(_tippecanoe_cache_args)
set(_tippecanoe_build_flags)

# Currently can't support building for Windows
if(WIN32)
  # If this ever gets done, it will likely require MINGW
  # so static link libgcc and libstdc++
  # (unless tippecanoe switches to CMake and compiling with works MSVC)
  set(_tippecanoe_build_flags "${_tippecanoe_build_flags} -static -static-libgcc -static-libstdc++")
endif()

if(CMAKE_OSX_ARCHITECTURES STREQUAL "x86_64")
  set(OSX_TARGET_FLAG "--target=x86_64-apple-macos10.9")
elseif(CMAKE_OSX_ARCHITECTURES STREQUAL "arm64")
  set(OSX_TARGET_FLAG "--target=arm64-apple-macos11")
else()
  set(OSX_TARGET_FLAG "")
endif()

# tippecanoe
set(TIPPECANOE_SOURCE_DIR ${CMAKE_BINARY_DIR}/TIPPECANOE-src)
set(TIPPECANOE_BINARY_DIR ${CMAKE_BINARY_DIR}/TIPPECANOE-build)
set(TIPPECANOE_URL "https://github.com/felt/tippecanoe/archive/refs/tags/${TIPPECANOE_VERSION}.zip")

set(TIPPECANOE_INSTALL_DIR ${CMAKE_BINARY_DIR}/TIPPECANOE-install)

# Makefile based builds on macOS are weird and painful when cross-compiling...
# Setting env vars was the only way that worked to get the a working --target option to the compiler
if(APPLE)
  if(CMAKE_OSX_ARCHITECTURES STREQUAL "x86_64")
    set(OSX_TARGET_FLAG "--target=x86_64-apple-macos10.14")
  elseif(CMAKE_OSX_ARCHITECTURES STREQUAL "arm64")
    set(OSX_TARGET_FLAG "--target=arm64-apple-macos11")
  else()
    set(OSX_TARGET_FLAG "")
  endif()
  ExternalProject_add(TIPPECANOE
    SOURCE_DIR ${TIPPECANOE_SOURCE_DIR}
    INSTALL_DIR ${TIPPECANOE_INSTALL_DIR}
    URL ${TIPPECANOE_URL}
    # URL_HASH "SHA256="
    CONFIGURE_COMMAND ""
    BUILD_COMMAND ${CMAKE_COMMAND} -E env CFLAGS="${OSX_TARGET_FLAG}" CXXFLAGS="${OSX_TARGET_FLAG}" make -j
    BUILD_IN_SOURCE ON
    INSTALL_COMMAND make -j install PREFIX=<INSTALL_DIR>
    )
else()
  # But other OSes have issues building with overriding those env vars to be empty
  ExternalProject_add(TIPPECANOE
    SOURCE_DIR ${TIPPECANOE_SOURCE_DIR}
    INSTALL_DIR ${TIPPECANOE_INSTALL_DIR}
    URL ${TIPPECANOE_URL}
    # URL_HASH "SHA256="
    CONFIGURE_COMMAND ""
    BUILD_COMMAND make -j
    BUILD_IN_SOURCE ON
    INSTALL_COMMAND make -j install PREFIX=<INSTALL_DIR>
    )
endif()

install(PROGRAMS ${TIPPECANOE_INSTALL_DIR}/bin/ DESTINATION bin)
install(FILES ${TIPPECANOE_INSTALL_DIR}/share/ DESTINATION share)
