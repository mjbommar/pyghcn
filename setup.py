from setuptools import setup, find_packages

setup(
    name='pyghcn',
    version='0.1.1',
    packages=find_packages(exclude=['*tests*']),
    package_dir={'': '.'},
    install_requires=[
        'geopy',
        'pandas',
        'requests',
    ],
    url='https://github.com/mjbommar/pyghcn',
    license='MIT License',
    author='Michael J Bommarito II',
    author_email='michael.bommarito@gmail.com',
    description='Python 3 client for the NOAA Global Historical Climatology Network (GHCN)',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='noaa ghcn weather climate dataset',

)
