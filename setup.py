from setuptools import setup

LONG_DESCRIPTION = """
Ordinal hashing of multidimensonal data and geographic coordinates via Morton coding / Z-ordering.

In mathematical analysis and computer science, `Z-order`, `Morton-order`, or a `Morton-code` is a function
which maps multidimensional data to one dimension while preserving locality of the data points.
It was introduced in 1966 by IBM researcher, G. M. Morton. The z-value of a point in multidimensions is
calculated by interleaving the binary representations of its coordinate values. Once the data are sorted
into this ordering, any one-dimensional data structure can be used, such as binary search trees, B-trees,
skip lists, or hash tables. The resulting ordering can equivalently be described as the order one would
achieve from a depth-first traversal of a quadtree, where `{x, y, ..., K}` are combined into a single
ordinal value that is easily compared, searched, and indexed against other Morton numbers.
"""


def build():
    setup(
            name='pymorton',
            version='1.0.7',
            author='Trevor Prater',
            author_email='trevor.prater@gmail.com',
            description='A lightweight morton coder with lat/long support.',
            long_description=LONG_DESCRIPTION,
            license='MIT',
            keywords='nearest neighbors, geo hashing, geo, z-order, morton coding, hashing',
            url='https://github.com/trevorprater/pymorton',
            packages=['pymorton'],
            python_requires='>=2.6',
            install_requires=[],
            classifiers=[
                'Development Status :: 5 - Production/Stable',
                'Topic :: Utilities',
                'License :: OSI Approved :: MIT License'
            ]
    )


if __name__ == '__main__':
    build()
