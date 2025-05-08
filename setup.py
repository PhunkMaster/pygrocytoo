import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pygrocytoo",
    version="0.0.0",
    author="PhunkMaster",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/phunkmaster/pygrocytoo",
    license="MIT",
    packages=setuptools.find_packages(),
    install_requires=[
        "requests",
        "deprecation~=2.1.0",
        "pydantic~=2.11",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
