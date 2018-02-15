# <div align="center">pymorton</div>

<p align="center">Ordinal hashing of multidimensonal data and geographic coordinates via <a href="https://en.wikipedia.org/wiki/Z-order_curve">Morton coding / Z-ordering</a>.</p>

# <div align="center">[![Codecov](https://img.shields.io/codecov/c/github/trevorprater/pymorton.svg)](https://codecov.io/gh/trevorprater/pymorton) [![Travis](https://img.shields.io/travis/trevorprater/pymorton.svg)](https://travis-ci.org/trevorprater/pymorton) [![Status](https://img.shields.io/badge/status-stable-brightgreen.svg)](https://travis-ci.org/trevorprater/pymorton) [![GitHub tag](https://img.shields.io/github/tag/trevorprater/pymorton.svg)]() [![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/trevorprater/pymorton/blob/master/LICENSE.md) </div>

<p align="center">
  <img src="https://i.imgur.com/WlMKO20r.jpg" height=10% width=100%>
</p>

In mathematical analysis and computer science, *Z-order*, *Morton-order*, or a *Morton-code* is a function which maps multidimensional data to one dimension while preserving locality of the data points. It was introduced in 1966 by IBM researcher, *[G. M. Morton](https://domino.research.ibm.com/library/cyberdig.nsf/papers/0DABF9473B9C86D48525779800566A39/$File/Morton1966.pdf)*. *The z-value* of a point in multidimensions is calculated by interleaving the binary representations of its coordinate values. Once the data are sorted into this ordering, any one-dimensional data structure can be used, such as binary search trees, B-trees, skip lists, or hash tables. The resulting ordering can equivalently be described as the order one would achieve from a depth-first traversal of a quadtree,
where `{x, y, ..., K}` are combined into a single ordinal value that is easily compared, searched, and indexed against other *Morton numbers*. 


*At the highest level, **pymorton** is split into two logical functions*:

  * **(de)interleave**: encodes/decodes hashes representing two or three dimensionsal integer sets. `{x, y, z ∈ Z}` or `{x, y ∈ Z}`, where `Z` represents all integer values.
  
  * **(de)interleave_latlng**: encodes and decodes hashes representing latitude and longitude.

<div style="page-break-after: always;"></div>

### Example usage scenario:
 * *Given a directory of images, **sort the images by color** (average RGB)*:
 
 
   ```python
   from statistics import mean
   from glob import glob
   from PIL import Image
   import pymorton

   imgs = [(fname, Image.open(fname)) for fname in glob('imgpath/*.jpg')[:100]]
   
   # for each image, generate a tuple of len==3, representing the image's average RGB value
   avg_rgb_values = [
       [int(mean(img.getdata(band))) for band in range(3)] for _, img in imgs]
   
   # using the average RGB values, compute the Z-order of each image
   hashed_imgs = list(zip([fname for fname, _ in imgs],
                      [pymorton.interleave(*avg_rgb) for avg_rgb in avg_rgb_values]))
   
   # returns a sorted-by-color list of photos found within the directory
   return sorted(hashed_imgs, key=lambda img_tuple: img_tuple[1])
   ```

While the above use-case is fairly uncommon in the context of *Morton-coding*, I believe it illustrates the utility of the algorithm quite well. *Morton-coding* is most commonly used within the realm of geospatial indexing, but its potential applications are infinite!


## Installation

via [pip](https://pypi.python.org/pypi/pymorton/0.1.0):
```bash
pip install pymorton
```


via [source](https://github.com/trevorprater/pymorton):
```bash
git clone https://github.com/trevorprater/pymorton.git
cd pymorton
python setup.py install
```


## Usage

* **3D-hashing**
```python
import pymorton as pm

mortoncode = pm.interleave(100, 200, 50)  # 5162080
mortoncode = pm.interleave3(100, 200, 50) # 5162080

pm.deinterleave3(mortoncode)              # (100, 200, 50)
```


* **2D-hashing**
```python
import pymorton as pm

mortoncode = pm.interleave(100, 200)     # 46224
mortoncode = pm.interleave2(100, 200)    # 46224

pm.deinterleave2(mortoncode)             # (100, 200)
```


* **geo-hashing**
```python
import pymorton as pm

geohash = pm.interleave_latlng(40.723471, -73.985361)     # '03023211233202130332202203002303'

pm.deinterleave_latlng(geohash)                           # (40.723470943048596, -73.98536103777587)
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

<div style="page-break-after: always;"></div>

## Tests

From the project's root directory, execute `nosetests`.

Please feel free to contact *trevor.prater@gmail.com* regarding any questions/comments/issues.


### References:

* [Z-order curve](https://en.wikipedia.org/wiki/Z-order_curve)
* [Implementation for the algorithm (1)](http://stackoverflow.com/a/18528775)
* [Implementation for the algorithm (2)](https://github.com/Forceflow/libmorton)
* [Extended explanation with different algorithms](http://www.forceflow.be/2013/10/07/morton-encodingdecoding-through-bit-interleaving-implementations/)


## License
MIT
