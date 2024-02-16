tippecanoe Python Distributions
===============================

[![PyPI](https://img.shields.io/pypi/v/tippecanoe.svg)](https://pypi.org/project/tippecanoe)

A project that packages [tippecanoe](https://github.com/felt/tippecanoe) as a Python package, enabling `tippecanoe` to be installed from PyPI:

```sh
pip install tippecanoe
```

or used as part of `build-system.requires` in a pyproject.toml file:

```toml
[build-system]
requires = ["tippecanoe"]
```

After installation, the Python bin directory for console scripts may need to be added to your path (or if installing in a venv, activate the venv).
Commands installed are: `tippecanoe`, `tile-join`, `tippecanoe-decode`, `tippecanoe-enumerate`, `tippecanoe-json-tool`, and `tippecanoe-overzoom`.

PyPI package versions will follow the `major.minor.patch` version numbers of tippecanoe releases.

Binary wheels for macOS and Linux for most CPU architectures supported on PyPI are provided. ARM wheels for Raspberry Pi available at https://www.piwheels.org/project/tippecanoe/.

[tippecanoe PyPI Package Homepage](https://github.com/nightlark/tippecanoe-pypi)

[tippecanoe Homepage](https://github.com/felt/tippecanoe)

[tippecanoe Source Code](https://github.com/felt/tippecanoe)

[tippecanoe License](https://github.com/felt/tippecanoe/blob/main/LICENSE.md): BSD 2-Clause "Simplified" License

Installing tippecanoe
=====================

tippecanoe can be installed by pip with:

```sh
pip install tippecanoe
```

or:

```sh
python -m pip install tippecanoe
```

Building from the source dist package requires internet access in order to download a copy of the tippecanoe source code.

Using with pipx
===============

Using `pipx run tippecanoe <args>` will run tippecanoe without any install step, as long as the machine has pipx installed (which includes GitHub Actions runners).

Using with pyproject.toml
=========================

tippecanoe can be added to the `build-system.requires` key in a pyproject.toml file for building Python extensions that use tippecanoe to when building wheels.

```toml
[build-system]
requires = ["tippecanoe"]
```

License
=======

The code for this project (for building the wheels) is covered by the [3-Clause BSD License](https://opensource.org/license/bsd-3-clause/).

tippecanoe is distributed under the [BSD 2-Clause "Simplified" License](https://github.com/felt/tippecanoe/blob/main/LICENSE.md). For more information about tippecanoe, visit [https://github.com/felt/tippecanoe](https://github.com/felt/tippecanoe)
