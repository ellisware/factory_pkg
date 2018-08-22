import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="factory_pkg",
    version="0.0.1",
    author="Mike Ellis",
    author_email="mike.ellis3@gmail.com",
    description="Modeling a OASREST API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ellisware",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
          'json','requests','urllib'
      ],
)