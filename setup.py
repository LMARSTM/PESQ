# 2019-May
# github.com/ludlows
# Python Wrapper for PESQ Score (narrowband and wideband)
from setuptools import find_packages
from setuptools import setup, Extension

with open("README.md", "r") as fh:
    long_description = fh.read()


class CyPesqExtension(Extension):
    def __init__(self, *args, **kwargs):
        self._include = []
        super().__init__(*args, **kwargs)

    @property
    def include_dirs(self):
        import numpy
        return self._include + [numpy.get_include()]

    @include_dirs.setter
    def include_dirs(self, dirs):
        self._include = dirs


extensions = [
    CyPesqExtension(
        "cypesq",
        ["pesq/cypesq.pyx", "pesq/dsp.c", "pesq/pesqdsp.c", "pesq/pesqmod.c"],
        include_dirs=['pesq'],
        define_macros=[("Py_LIMITED_API", "0x030B0000")],
        py_limited_api=True,
        language="c")
]
setup(
    name="pesq",
    version="0.0.5",
    author="ludlows",
    description="Python Wrapper for PESQ Score (narrow band and wide band)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ludlows/PESQ",
    packages=find_packages(),
    package_data={'pesq': ["*.pyx", "*.h", "dsp.c", "pesqdsp.c", "pesqmod.c"]},
    ext_package='pesq',
    ext_modules=extensions,
    python_requires=">=3.11",
    setup_requires=['setuptools>=18.0', 'cython>=3.1', 'numpy'],
    install_requires=['numpy'],
    options={"bdist_wheel": {"py_limited_api": "cp311"}},
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
