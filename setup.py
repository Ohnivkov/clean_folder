from setuptools import setup, find_namespace_packages
import os
r=os.path.abspath('sort.py')
setup(
    name='clean_folder',

    packages=find_namespace_packages(),
    install_requires=['markdown'],
    entry_points={'console_scripts': ['clean-folder=clean_folder.sort:main']}

)
