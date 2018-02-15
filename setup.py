from setuptools import setup

with open('DESCRIPTION.txt') as f:
    long_description = f.read()

def build():
    setup(
            name='pymorton',
            version='1.0.4',
            author='Trevor Prater',
            author_email='trevor.prater@gmail.com',
            description='A lightweight morton coder with lat/long support.',
            long_description=long_description,
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
