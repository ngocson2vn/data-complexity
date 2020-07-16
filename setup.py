import setuptools
import dcm

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="data-complexity",
    version=dcm.VERSION,
    author="Son Nguyen",
    license="MIT",
    author_email="ngocson2vn@gmail.com",
    description="Data Complexity Measures",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ngocson2vn/data-complexity",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "numpy",
        "gower"
    ]
)
