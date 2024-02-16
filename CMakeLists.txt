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

# tippecanoe
set(TIPPECANOE_SOURCE_DIR ${CMAKE_BINARY_DIR}/TIPPECANOE-src)
set(TIPPECANOE_BINARY_DIR ${CMAKE_BINARY_DIR}/TIPPECANOE-build)

set(TIPPECANOE_INSTALL_DIR ${CMAKE_BINARY_DIR}/TIPPECANOE-install)
ExternalProject_add(TIPPECANOE
  SOURCE_DIR ${TIPPECANOE_SOURCE_DIR}
  INSTALL_DIR ${TIPPECANOE_INSTALL_DIR}
  URL "https://github.com/felt/tippecanoe/archive/refs/tags/${TIPPECANOE_VERSION}.zip"
  # URL_HASH "SHA256="
  CONFIGURE_COMMAND ""
  BUILD_COMMAND make -j
  BUILD_IN_SOURCE ON
  INSTALL_COMMAND make -j install PREFIX=<INSTALL_DIR>
  )
install(PROGRAMS ${TIPPECANOE_INSTALL_DIR}/bin/ DESTINATION bin)
install(FILES ${TIPPECANOE_INSTALL_DIR}/share/ DESTINATION share)
