You are a dinosaur, and you have to dodge the meteors by moving the mouse. If a meteor hits you, you lose a life. Hopefully, you always can eat a ham to recover some lives.

I made this game to learn how to use `pygame` in my 2nd year of my studies. I recently updated it to support Python 3, and to polish a bit the project (mainly translating the comments and code into English).

I also left the original one in `first_version` folder just for the old times :D

## Installation
This app is uploaded in https://pypi.org/. To install and run it, you just need to:
```
pip install dinosaur-pygame
dinosaur_pygame  # The game is installed as a script, just needs to run that command for the game to start.
```

## Local Development
You may need to [install some prerequisites](https://www.pygame.org/wiki/GettingStarted) to make `pygame` work. Once they are installed, to install the project:
```
make install
```

#### To run the application:
```
make run
```

#### To install the package and check if it works before publishing the new version into https://pypi.org/:
```
make package_install
dinosaur_pygame  # checks if it runs properly in the console. Run this with your venv activated.
```
Good starting documentation for pypi packages: https://packaging.python.org/tutorials/packaging-projects/ and https://python-packaging.readthedocs.io/en/latest/command-line-scripts.html#the-console-scripts-entry-point.

#### To publish the new package in test pypi
```
make upload_package_to_test_pypi  # it requires your token
python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps dinosaur-pygame
dinosaur_pygame  # Run the app
```


## Art
For the new version, I got the images from https://opengameart.org/:
- Background: https://opengameart.org/content/sky-tiles
- Dinosaur: https://opengameart.org/content/dinosaur-0
- Meteor: https://opengameart.org/content/meteor-animated-64x64
- Ham: https://opengameart.org/content/32x32-food-set

Author: Alberto Morales
