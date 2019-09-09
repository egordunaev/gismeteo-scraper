import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gis-meteo-scraper",
    version="0.0.1",
    author="Egor Dunaev",
    author_email="egodunaev@gmail.com",
    description="A simple web scraper for gismeteo.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/egordunaev/gismeteo-scraper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['requests', 'bs4'],

)