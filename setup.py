from setuptools import setup, find_packages


setup(
    name="wecat",
    version="0.1",
    packages=find_packages(),
    package_dir={"": "."},
    install_requires=[],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
    zip_safe=True,
)
