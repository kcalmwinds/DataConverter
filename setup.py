import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kcalmwinds",  # Replace with your own username
    version="0.1.1",
    author="Mark J Cameron",
    author_email="kcalmwinds@gmail.com",
    description="Convert all of your bytes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kcalmwinds/dataconverter",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
