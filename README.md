# pymorton

A simple morton coding library with geo-hashing support.

## Installation

```
pip install pymorton
```

## Tests

Simply run:
```
nosetests
```

## Usage

```python

import pymorton as pm

# three-dimensional hashing example
#####################################################
hash = pm.interleave(100, 200, 50)
# or
hash = pm.interleave3(100, 200, 50)
pm.deinterleave3(hash) #returns (100, 200, 50)
#####################################################

# two-dimensional hashing example
#####################################################
hash = pm.interleave(100, 200)
# or
hash = pm.interleave2(100, 200)
pm.deinterleave2(hash) #returns (100, 200)
#####################################################
 
# geohashing example
#####################################################
geohash = pm.interleave_latlng(40.723471, -73.985361)

# returns (40.723470943048596, -73.98536103777587)
pm.deinterleave_latlng(geohash) 
#####################################################
```

## API
- `pymorton.interleave(**args)`
    * description: Hashes x, y or x, y, z into a single value.
                   Wraps interleave2() and interleave3().

- `pymorton.interleave2(x, y)`
    * description: Returns a hash (int) representing `x, y`.

- `pymorton.interleave3(x, y, z)`
    * description: Returns a hash (int)\nrepresenting `x, y, z`.

- `pymorton.interleave_latlng(lat, lng)`
    * description: Returns a hash (string base-4)
                   representing `lat, lng`.

- `pymorton.deinterleave2(n)`
    * description: Returns a tuple representing the arguments to
                   the corresponding interleave2() call.

- `pymorton.deinterleave3(n)`
    * description: Returns a tuple representing the arguments to
                   the corresponding interleave3() call.

- `pymorton.deinterleave_latlng(lat, lng)`
    * description: Returns a tuple representing the arguments to
                   the corresponding interleave_latlng() call.

## License
MIT
