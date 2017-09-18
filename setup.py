from setuptools import setup

CLASSIFIERS = [
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: BSD License',
    'Programming Language :: Python',
    'Operating System :: OS Independent',
    'Topic :: Scientific/Engineering :: Atmospheric Science',
]

setup(
    name = "",
    version = "0.1",
    url = "https://ouranosinc.github.io/pavics-sdi/",
    install_requires = [
        'flyingpigeon',
        'malleefowl',
        'pavics_datacatalog'
    ],
    author="CRIM/Ouranos",
    author_email="pavics@ouranos.ca",
    description="Scientific gateway for climate data analytics.",
    long_description=open('README.rst', 'rt').read(),
    license="BSD",
    classifiers=CLASSIFIERS,
)
