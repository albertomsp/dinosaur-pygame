install:
	( \
		python3 -m venv .venv; \
		source .venv/bin/activate; \
		pip3 install -r dinosaur_pygame/requirements.txt; \
		pip install --upgrade pip; \
	)

clean:
	rm -rf .venv dist build

run:
	source .venv/bin/activate && python3 dinosaur_pygame/main.py

make run_original:
	source .venv/bin/activate && cd dinosaur_pygame/first_version && python3 dinosaurio.py

test_pygame:
	source .venv/bin/activate && python3 -m pygame.examples.aliens

mac_install:
	brew update
	brew install mercurial
	brew install sdl sdl_image sdl_mixer sdl_ttf portmidi
	brew install smpeg
	brew install sdl2 sdl2_gfx sdl2_image sdl2_mixer sdl2_net sdl2_ttf

install_package:
	source .venv/bin/activate && python3 setup.py install && dinosaur_pygame

upload_package_to_test_pypi:
	( \
		source .venv/bin/activate; \
		python3 -m pip install --upgrade setuptools wheel; \
		python3 setup.py sdist bdist_wheel; \
		python3 -m pip install --upgrade twine; \
		python3 -m twine upload --config-file .pypirc --repository testpypi dist/* ; \
		pip install -i https://test.pypi.org/simple/ dinosaur-pygame==0.0.7; \
		dinosaur_pygame; \
	)
	# Needs .pypirc file - it can be created from the template `pypirc_template`

upload_package_to_pypi:
	( \
		source .venv/bin/activate; \
		python3 -m pip install --upgrade setuptools wheel; \
		python3 setup.py sdist bdist_wheel; \
		python3 -m pip install --upgrade twine; \
		python3 -m twine upload --config-file .pypirc --repository pypi dist/*; \
	)
	# Needs .pypirc file - it can be created from the template `pypirc_template`

