#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os

from setuptools import find_packages

# try:
#     from skbuild import setup
# except ImportError:
#     sys.stderr.write("""scikit-build is required to build from source or run tox.
# Please run:
#   python -m pip install scikit-build
# """)
#     # from setuptools import setup
#     sys.exit(1)
from setuptools import setup


with open('README.rst', 'rt') as readme_file:
    readme = readme_file.read()


def prerelease_local_scheme(version):
    """
    Return local scheme version unless building on master in CircleCI.

    This function returns the local scheme version number
    (e.g. 0.0.0.dev<N>+g<HASH>) unless building on CircleCI for a
    pre-release in which case it ignores the hash and produces a
    PEP440 compliant pre-release version number (e.g. 0.0.0.dev<N>).
    """
    from setuptools_scm.version import get_local_node_and_date

    if os.getenv('CIRCLE_BRANCH') in {'master'}:
        return ''
    else:
        return get_local_node_and_date(version)


setup(
    name='ptc',
    use_scm_version={'local_scheme': prerelease_local_scheme},
    description='Kaggle glomerulus segmentation',
    long_description=readme,
    long_description_content_type='text/x-rst',
    author='Computational Microscopy Imaging Laboratory, UF',
    author_email='sayat.mimar@medicine.ufl.edu',
    url='https://github.com/SarderLab/Kaggle_Glom_Segmentaion',
    packages=find_packages(exclude=['tests', '*_test']),
    package_dir={
        'kaggle': 'kaggle',
    },
    include_package_data=True,
    install_requires=[
        # scientific packages
        'nimfa>=1.3.2',
        'numpy==1.24.4',
        'scipy>=0.19.0',
        'Pillow==9.5.0',
        'pandas>=0.19.2',
        'imageio>=2.3.0',
        'shapely[vectorized]',
        #'opencv-python-headless<4.7',
        #'sqlalchemy',
        # 'matplotlib',
        # 'pyvips',
        'termcolor',
        'seaborn',
        'opencv-python',
        'openslide-python',
        'scikit-image==0.19.2',
        'scikit-learn==1.0.2',
        'lxml==4.8.0',
        'joblib==1.1.0',
        'tifffile==2023.4.12',
        'tiffslide==1.5.0',
        'tqdm==4.64.0',
        'umap-learn==0.5.3',
        # 'openpyxl',
        # 'xlrd<2',
        # dask packages
        'dask[dataframe]>=1.1.0',
        'distributed>=1.21.6',
        # large image sources
        #'large-image[sources]',
        'girder-slicer-cli-web',
        'girder-client',
        # cli
        'ctk-cli',
        'aicsimageio==4.9.2',
        'bfio==2.3.0',
        'scikit-build==0.15.0',
        'albumentations==1.2.1',
        'ipywidgets==7.7.1',
        'nvidia-ml-py==11.515.48',
        'munch==2.5.0',
        'opencv-python-headless==4.6.0.66',
        'rasterio==1.3.0',
    ],
    license='Apache Software License 2.0',
    keywords='kaggle',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    zip_safe=False,
)