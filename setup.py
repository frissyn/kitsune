import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kitsune.py",
    version="0.0.1a",
    author="frissyn",
    author_email="author@example.com",
    description="A simple and extensible Python API wrapper for Kitsu.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/frissyn/kitsune",
    packages=["reflux"],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 2 - Pre-Alpha",
    ],
    python_requires='>=3.6',
)
