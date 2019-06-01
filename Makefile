setup: 
	apt-get -y install python-dev python-setuptools python3-dev python-virtualenv cmake
	apt-get -y install libtiff5-dev libjpeg62-turbo-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk python3-tk libharfbuzz-dev libfribidi-dev
	apt-get -y install supervisor
	echo >> etc/supervisor/supervisord.conf && cat ./supervisor.conf >> etc/supervisor/supervisord.conf

init:
	pip install -r requirements.txt

test:
	python -m unittest discover -v ./src

server:
	./external/openpixelcontrol/bin/gl_server -l layouts/opc.json </dev/null &>/dev/null &

start:
	python src/process.py

docs:
	cd docs && $(MAKE) singlehtml

.PHONY: init test start docs Makefile