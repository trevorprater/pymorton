# pymorton

A simple library that enables Morton coding/hashing with built-in geo-hashing support.

Interleaved bits (aka Morton numbers) are useful for linearizing K-dimensional integer coordinates, so `x, y ... K` are combined into a single number that is easily compared, searched, and indexed in addition to being ordinally close to a Morton number that represents a point nearby to `x, y ... K`.

<p align="center">
  <img src="http://asgerhoedt.dk/wp-content/uploads/2012/10/MortonCurve-8x8x8.png">
</p>
>In mathematical analysis and computer science, Z-order, Morton order, or Morton code is a function which maps multidimensional data to one dimension while preserving locality of the data points. It was introduced in 1966 by G. M. Morton. The z-value of a point in multidimensions is simply calculated by interleaving the binary representations of its coordinate values. Once the data are sorted into this ordering, any one-dimensional data structure can be used such as binary search trees, B-trees, skip lists or (with low significant bits truncated) hash tables. The resulting ordering can equivalently be described as the order one would get from a depth-first traversal of a quadtree... ([Wikipedia](https://en.wikipedia.org/wiki/Z-order_curve))


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

From the root directory, execute `nosetests`.

## Usage

* **geo-hashing**
```python
import pymorton as pm

geohash = pm.interleave_latlng(40.723471, -73.985361) # returns '03023211233202130332202203002303'

pm.deinterleave_latlng(geohash)                       # returns (40.723470943048596, -73.98536103777587)
```


* **3D-hashing**
```python
import pymorton as pm

mortoncode = pm.interleave(100, 200, 50)  # returns 5162080
# or
mortoncode = pm.interleave3(100, 200, 50) # returns 5162080

pm.deinterleave3(mortoncode)              # returns (100, 200, 50)
```


* **2D-hashing**
```python
import pymorton as pm

mortoncode = pm.interleave(100, 200)     # returns (46224)
# or
mortoncode = pm.interleave2(100, 200)    # returns (46224)

pm.deinterleave2(mortoncode)             # returns (100, 200)
```


## API
- `pymorton.interleave(*args)`
    * Hashes `x, y` or `x, y, z` into a single value.
                   This function wraps interleave2() and interleave3() by supporting variable-length args.

- `pymorton.interleave2(x, y)`
    * Returns a hash (int) representing `x, y`.

- `pymorton.interleave3(x, y, z)`
    * Returns a hash (int) representing `x, y, z`.

- `pymorton.interleave_latlng(lat, lng)`
    * Returns a hash (string base-4)
                   representing `lat, lng`.

- `pymorton.deinterleave2(hash)`
    * Returns a tuple representing the arguments to
                   the corresponding interleave2() call.

- `pymorton.deinterleave3(hash)`
    * Returns a tuple representing the arguments to
                   the corresponding interleave3() call.

- `pymorton.deinterleave_latlng(hash)`
    * Returns a tuple representing the arguments to
                   the corresponding interleave_latlng() call.

## License
MIT
