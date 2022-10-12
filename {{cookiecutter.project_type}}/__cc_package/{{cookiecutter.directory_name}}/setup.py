import setuptools

from {{cookiecutter.pkg_name}}.__version__ import __version__

setuptools.setup(
    name="{{cookiecutter.pkg_name}}",
    version=__version__,
    author="{{cookiecutter.author}}",
    author_email="",
    description="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8,<4.0",
)
