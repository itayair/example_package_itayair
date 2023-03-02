import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "example_package_itayair",
    version = "0.0.4",
    author = "Itay Yair",
    author_email = "iy24592@gmail.com",
    description = "A simple Python package",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    license='MIT',
    url = "https://github.com/itayair//example_package_itayair",
    project_urls = {
        "Bug Tracker": "https://github.com/itayair/example_package_itayair/-/issues",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # package_dir = {"": "src"},
    packages = setuptools.find_packages(),
    python_requires = ">=3.6"
)