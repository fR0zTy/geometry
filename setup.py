import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="geometry",
    version="0.0.1",
    author="fr0zty",
    author_email="darshn0108@gmail.com",
    description="Objects and utilities for grometry",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fR0zTy/geometry.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)