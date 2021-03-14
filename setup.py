import setuptools

with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="minimus_data_retrieve",
    version="0.0.dev0",

    description="minimus-data-retrieve",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="Odyssey Geophysics",

    package_dir={"": "src"},
    packages=setuptools.find_packages(where="./src"),

    install_requires=[
    ],

    python_requires=">=3.8",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "License :: OSI Approved :: Apache Software License",

        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)
