# pymorton

A simple library that enables Morton coding/hashing with built-in geo-hashing support.

In mathematical analysis and computer science, Z-order, Morton-order, or a Morton-code is a function which maps multidimensional data to one dimension while preserving locality of the data points. It was introduced in 1966 by IBM researcher, [G. M. Morton](https://domino.research.ibm.com/library/cyberdig.nsf/papers/0DABF9473B9C86D48525779800566A39/$File/Morton1966.pdf). The z-value of a point in multidimensions is calculated by interleaving the binary representations of its coordinate values. Once the data are sorted into this ordering, any one-dimensional data structure can be used, such as binary search trees, B-trees, skip lists, or hash tables. The resulting ordering can equivalently be described as the order one would achieve from a depth-first traversal of a quadtree.


In the context of linearizing K-dimensional integer coordinates, *Morton numbers* are very useful: **`{x, y, ..., K}`** are combined into a single ordinal value that is easily compared, searched, and indexed against other *Morton numbers*, where the inputs, **`{x, y, ..., K}`**, exist in the domain of integers, **`{x, y, ..., K ∈ Z}`**.

*For example, assume that you need to **sort a corpus of images by average *RGB* pixel value**: *Morton-coding* provides a simple solution to this problem via the generation of a *(hash)* for each image that represents its *average RGB* tuple within a single ordinal integer value.*

This algorithm has many practical applications, ranging from geospatial search to computer vision.

<p align="center">
  <img src="http://asgerhoedt.dk/wp-content/uploads/2012/10/MortonCurve-8x8x8.png">
</p>


Useful references:

* [Z-order curve](https://en.wikipedia.org/wiki/Z-order_curve)
* [Implementation for the algorithm (1)](http://stackoverflow.com/a/18528775)
* [Implementation for the algorithm (2)](https://github.com/Forceflow/libmorton)
* [Extended explanation with different algorithms](http://www.forceflow.be/2013/10/07/morton-encodingdecoding-through-bit-interleaving-implementations/)

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
