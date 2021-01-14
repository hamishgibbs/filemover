import setuptools

setuptools.setup(
    name="process_fb",
    version="0.0.1",
    author="Hamish Gibbs",
    author_email="Hamish.Gibbs@lshtm.ac.uk",
    description="Utilities for managing Facebook Data For Good data workflow.",
    url="https://github.com/hamishgibbs/fbprocess",
    install_requires=[
        'pandas',
    ],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6"
)
