# Luminous Bloom

An Ignite! granted funded project.

[![PyPI pyversions](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)

## Todo:

- [x] Gamma corrected color wheel func
- [x] All tentacles swipe up
- [ ] All tentacles fill up
- [ ] All tentacles strobe up
- [ ] Stripe with direction
- [ ] Swirl with direction

## Requirements

- python3.6

## Setup

This project uses neopixels, fadecandy, and opc.

### Development

#### OPC (OpenPixelControl)

Clone https://github.com/zestyping/openpixelcontrol and follow setup instructions. If using macOS ensure that CLI tools are accessible.

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
