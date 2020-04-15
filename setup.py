import os
import re
import pathlib
from setuptools import setup, find_packages
from miyadaiku import setuputils

DIR = pathlib.Path(__file__).resolve().parent


requires = [
    "miyadaiku",
    "miyadaiku_theme_jquery",
    "miyadaiku_theme_popper_js",
]

srcdir = DIR / 'node_modules/bootstrap/dist'
destdir = DIR / 'miyadaiku_theme_bootstrap4/externals'
copy_files = [
    [srcdir/ 'css/', ['bootstrap.css', 'bootstrap.min.css', ], destdir / 'css/'],
    [srcdir / 'js/', ['bootstrap.css', '*.js', ], destdir / 'js/']
]

versionpy = DIR / 'miyadaiku_theme_bootstrap4/__version__.py'
version = re.search(r'"([\d.]+)"', versionpy.read_text())[1]

setup(
    name="miyadaiku_theme_bootstrap4",
    version=version,
    author="Atsuo Ishimoto",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    description='Bootstrap 4 files for miyadaiku static site generator',
    long_description=setuputils.read_file(DIR, 'README.rst'),
    url='https://github.com/miyadaiku/miyadaiku-theme-bootstrap4',
    project_urls={
        'Miyadaiku': 'https://miyadaiku.github.io/',
    },

    packages=list(setuputils.list_packages(DIR, 'miyadaiku_theme_bootstrap4')),
    package_data={
        '': setuputils.SETUP_FILE_EXTS,
    },
    install_requires=requires,
    include_package_data=True,
    zip_safe=False,
    cmdclass={'copy_files': setuputils.copy_files},
    copy_files=copy_files
)
