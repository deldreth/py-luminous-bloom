# Luminous Bloom

An Ignite! granted funded project.

[![PyPI pyversions](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)

## Todo:

- [x] Gamma corrected color wheel func
- [x] All tentacles swipe up
- [x] All tentacles fill up
- [ ] Tentacles can receive repeating patterns
- [ ] All tentacles strobe up
- [x] Stripe with direction
- [x] Swirl with direction
- [x] Any tentacle fades
- [x] Different tentacles fade
- [x] Sparkle
- [ ] Shimmer
- [x] Pulsing shimmer
- [x] Ripple

### Timing:

- [ ] Effects expressed in seconds/minutes

## Requirements

- python3.6

## Setup

This project uses neopixels, fadecandy, and opc.

### Development

#### Clone with Externals

This repo includes a submodule: https://github.com/zestyping/openpixelcontrol

When cloning be sure to:

```
git clone --recursive
```

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
