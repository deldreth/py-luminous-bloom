# Luminous Bloom

An Ignite! granted funded project.

[![PyPI pyversions](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)

- [Media](#media)
  - [YouTube](#youtube)
- [Todo](#todo)
- [Setup](#setup)
  - [Installation](#installation)
    - [Raspberry Pi (Raspbian Stretch)](#raspberry-pi--raspbian-stretch-)
    - [Setup Luminous Bloom](#setup-luminous-bloom)
    - [Setup supervisor](#setup-supervisor)
  - [Development](#development)
    - [OPC (OpenPixelControl)](#opc--openpixelcontrol-)
    - [Running Tests](#running-tests)
    - [Running](#running)
- [Colors](#colors)
  - [Ranges](#ranges)

## Media

### YouTube

![Test 1](https://youtu.be/UHGA_CBlYU4)
![Test 2](https://youtu.be/GV5ze9NrJMw)
![Test 3](https://youtu.be/7AvBYTMB8QI)

## Todo

- [x] Gamma corrected color wheel func
- [x] All tentacles swipe up
- [x] All tentacles fill up
- [x] Tentacles can receive repeating patterns
- [x] Stripe with direction
- [x] Swirl with direction
- [x] Any tentacle fades
- [x] Different tentacles fade
- [x] Sparkle
- [x] Shimmer
- [x] Pulsing shimmer
- [x] Ripple
- [x] Finish animations
- [x] Animations expressed in seconds/minutes
- [x] Raspberry Pi Setup
- [x] Supervisor Setup
- [x] Duration test (Approx. 20 hours)

## Setup

This project uses neopixels, fadecandy, and opc.

This repo includes two submodule:

- https://github.com/zestyping/openpixelcontrol
- https://github.com/scanlime/fadecandy

When cloning be sure to:

```
git clone --recursive
```

### Installation

#### Raspberry Pi (Raspbian Stretch)

_Raspberry PI setup assumes that the default user `pi` is used._

Install env and required libs:

```
sudo apt-get -y install python-dev python-setuptools python3-dev python-virtualenv cmake

sudo apt-get -y install libtiff5-dev libjpeg62-turbo-dev zlib1g-dev   libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk python3-tk libharfbuzz-dev libfribidi-dev
```

#### Setup Luminous Bloom

cd into the cloned project directory and install the pip requirements.

```
pip install -r requirements.txt
```

#### Setup supervisor

Install supervisord and supervisorctl.

_supervisor could be installed manually through pip but it's also available through apt._

```
sudo apt-get install supervisor
```

Append the contents of (supervisor.conf)[./supervisor.conf] to `/etc/supervisor/supervisord.conf` (or wherever a supervisor config is located).

Retstart supervisor:

```
sudo service supervisor restart
```

If everything is working correctly running `sudo supervisorctl status` should provide output of two running processes.

```
pi@raspberrypi:~ $ sudo supervisorctl status
fadecandy                        RUNNING   pid 11489, uptime 10:54:42
luminousbloom                    RUNNING   pid 11490, uptime 10:54:42
```

That's it! Plug in the fadecandy and watch the magic.

### Development

#### OPC (OpenPixelControl)

If using macOS ensure that CLI tools are accessible.

```
$ cd external/openpixelcontrol
$ make
```

```
./external/openpixelcontrol/bin/gl_server -l ./layouts/opc.json
```

#### Running Tests

```
python -m unittest discover -v ./src
```

#### Running

```
python src/luminous-bloom.py
```

## Colors

This library depends upon the Colours library and extends that library's class to provide a few utilities where rgb values are needed from 0..255 instead of 0..1.

### Ranges

Color ranges can be approximated with HSL values between two colors...

```python
# a list of 5 colors stepped between red and blue
colors = list(Color("red").range_to(Color("blue"), 5))
```
