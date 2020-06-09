install:
	( \
		python3 -m venv .venv; \
		source .venv/bin/activate; \
		cd lib/dinosaur_pygame/; \
		pip3 install -r requirements.txt; \
		deactivate; \
	)

clean:
	rm -r .venv
	rm -r .dist
	rm -r .build

run:
	source .venv/bin/activate && cd lib/dinosaur_pygame/ &&  python3 __main__.py

make run_original:
	source .venv/bin/activate && cd lib/dinosaur_pygame/first_version && python3 dinosaurio.py

test_pygame:
	source .venv/bin/activate && python3 -m pygame.examples.aliens

mac_install:
	brew update
	brew install mercurial
	brew install sdl sdl_image sdl_mixer sdl_ttf portmidi
	brew install smpeg
	brew install sdl2 sdl2_gfx sdl2_image sdl2_mixer sdl2_net sdl2_ttf

package_install:
	source .venv/bin/activate && python3 -m pip install --user --upgrade setuptools wheel && python3 setup.py sdist bdist_wheel && python3 setup.py install && dinosaur_pygame

