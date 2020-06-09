import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dinosaur-pygame",
    version="0.0.9",
    entry_points={
        'console_scripts': [
            'dinosaur_pygame=dinosaur_pygame.main:main',
        ],
    },
    author="Alberto Morales",
    author_email="albertomoralessp@gmail.com",
    description="A dinosaur game made with pygame",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/albertomsp/dinosaur-pygame",
    packages=setuptools.find_packages(),
    install_requires=[
        'pygame>=2.0.0.dev4',
    ],
    package_data={
        'dinosaur_pygame': ['dinosaur_pygame'],
    },
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
