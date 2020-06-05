install:
	# mac_install first TODO
	python3 -m venv .venv
	source .venv/bin/activate
	pip3 install -r requirements.txt

clean:
	rm -r .venv

run:
	python3 main.py

test_pygame:
	python3 -m pygame.examples.aliens

mac_install:
	brew update
	brew install mercurial
	brew install sdl sdl_image sdl_mixer sdl_ttf portmidi
	brew install smpeg
	brew install sdl2 sdl2_gfx sdl2_image sdl2_mixer sdl2_net sdl2_ttf
