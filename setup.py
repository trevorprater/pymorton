from setuptools import setup

def build():
    setup(
            name = 'pymorton',
            version = '0.2.1',
            author = 'Trevor Prater',
            author_email = 'trevor.prater@gmail.com',
            description = 'A lightweight morton coder with lat/long support.',
            license = 'MIT',
            keywords = 'nearest neighbors, geo hashing, geo, z-order, morton coding, hashing',
            url = 'https://github.com/trevorprater/pymorton',
            packages = ['pymorton'],
            install_requires = [],
            classifiers = [
                'Development Status :: 3 - Development',
                'Topic :: Utilities',
                'License :: OSI Approved :: MIT License'
            ]
    )

if __name__ == '__main__':
    build()
