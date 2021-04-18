from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='WaveGenPy',
    version='0.1.0',
    description='Wave file generator',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/EfiPy/WaveGenPy',
    author='MaxWu',
    author_email='EfiPy.Core@gmail.com',
    classifiers=[
        'License :: Other/Proprietary License',
        'Development Status :: 3 - Alpha',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Testing :: Unit',
        'Topic :: Multimedia :: Sound/Audio :: Sound Synthesis',
        'Topic :: Scientific/Engineering :: Mathematics',
    ],

    package_dir={'': 'src'},
    packages = find_packages('src'),
    python_requires='>=3.5, <4',
)
