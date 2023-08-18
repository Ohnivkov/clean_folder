from setuptools import setup, find_namespace_packages
setup(
    name='clean_folder1',

    packages=find_namespace_packages(),
    install_requires=['markdown'],
    entry_points={'console_scripts': ['clean-folder=clean_folder1.sort:main']}

)
