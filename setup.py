# Created by Adam Thompson-Sharpe on 12/03/2020.
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as r:
    requirements = r.read().split("\n")

setuptools.setup(
    name="pywca",
    version="1.0.0",
    author="Adam Thompson-Sharpe",
    author_email="adamthompsonsharpe@gmail.com",
    description="A third-party web scraper API to view and interact with the World Cube Association website.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MysteryBlokHed/PyWCA",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.6"
)
