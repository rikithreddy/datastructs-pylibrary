import setup
setup(
)import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rikithreddy",
    version="0.0.1",
    author="Rikith Reddy",
    author_email="rikithreddy03@gmail.com",
    # TODO: Add description
    # description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rikithreddy/datastructs-pylibrary",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)