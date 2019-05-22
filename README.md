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
- [Structure](#structure)
  - [Process](#process)
  - [Animations](#animations)
  - [Tentacles](#tentacles)
  - [Bloom](#bloom)
    - [Transitions](#transitions)
  - [Colors](#colors)
    - [Patterns](#patterns)
    - [Ranges](#ranges)

## Media

### YouTube

[Test 1](https://youtu.be/UHGA_CBlYU4)

[Test 2](https://youtu.be/GV5ze9NrJMw)

[Test 3](https://youtu.be/7AvBYTMB8QI)

## Todo

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
python src/process.py
```

## Structure

### Process

Entry point to start the animations. All available animations are part of a list of tuples. The first item of the tuple is a reference to the animation function, the second item is either the parameters to pass to the function or a lambda that will be executed (usually for dynamic/randomized parameters).

The process will run through the entire list of animations, randomized. Once it has finished the last it will reset and start again.

### Animations

The `animations` package contains multi functions used to sequence a series of bloom transitions. It also specifies the colors available to the LEDs and deals with timing for most animations.

### Tentacles

Analogous to a strand of LEDs. Each tentacle is 64 pixels in length, has a start and end pixel, and some notion of "which" tentacle it is.

Tentacles can patternize and colorize the pixels they contain relative to the whole list of pixels. There are also safety methods like `contains` to determine if a pixel value exists on a tentacle.

### Bloom

The `bloom.bloom` package contains all the pixel information, references to tentacles, and all the transitions available to animations. In general, transitions are choreographed list traversal algorithms that selectively set colors by mapping a value relative to a tentacle's pixel.

#### Transitions

**Images**, the `./images` directory contains a number if images used in transitions. These are read vertically from top to bottom. Each line's pixels mapped to a pixel on a tentacle.

### Colors

This library depends upon the Colours library and extends that library's class to provide a few utilities where rgb values are needed from 0..255 instead of 0..1. The Colours library provies a range_to method to calculate the colors between two colors.

```python
# a generator of 5 colors stepped between red and blue
colors = Color("Red").range_to(Color("Blue"), 5)
```

The `bloom.color` package contains two utlity classes: Pattern and Range. Both of which are deques intended to be used for higher performance list rotation operations.

#### Patterns

Patterns are deques composed of a single color or list of colors separated by black, all of the same length. For instance, a pattern created with White and length of 5 would create a deque in the shape of:

```python
pattern = Pattern(5, Colors("White"))
# pattern => ([(White), (White), (White), (White), (White), (Black), (Black), (Black), (Black), (Black), (White), (White), (White), (White), (White), ...])
```

#### Ranges

A deque composed of a list of colors.
