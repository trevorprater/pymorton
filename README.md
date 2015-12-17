# pymorton

A simple morton coding library with geo-hashing support.

![](https://upload.wikimedia.org/wikipedia/commons/d/da/Lebesgue-3d-step3.png)

In mathematical analysis and computer science, Z-order, Morton order, or Morton code is a function which maps multidimensional data to one dimension while preserving locality of the data points. It was introduced in 1966 by G. M. Morton.[1] The z-value of a point in multidimensions is simply calculated by interleaving the binary representations of its coordinate values. Once the data are sorted into this ordering, any one-dimensional data structure can be used such as binary search trees, B-trees, skip lists or (with low significant bits truncated) hash tables. The resulting ordering can equivalently be described as the order one would get from a depth-first traversal of a quadtree. ([Wikipedia](https://en.wikipedia.org/wiki/Z-order_curve))


## Installation

```
pip install pymorton
```
or
```
git clone https://github.com/trevorprater/pymorton.git
cd pymorton
python setup.py install
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
    * description: Returns a hash (int) representing `x, y, z`.

- `pymorton.interleave_latlng(lat, lng)`
    * description: Returns a hash (string base-4)
                   representing `lat, lng`.

- `pymorton.deinterleave2(hash)`
    * description: Returns a tuple representing the arguments to
                   the corresponding interleave2() call.

- `pymorton.deinterleave3(hash)`
    * description: Returns a tuple representing the arguments to
                   the corresponding interleave3() call.

- `pymorton.deinterleave_latlng(hash)`
    * description: Returns a tuple representing the arguments to
                   the corresponding interleave_latlng() call.

## License
MIT
