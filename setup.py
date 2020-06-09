import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dinosaur-pygame",
    version="0.0.3",
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
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
