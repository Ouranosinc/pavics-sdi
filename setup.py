from setuptools import setup

CLASSIFIERS = [
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: BSD License",
    "Programming Language :: Python",
    "Operating System :: OS Independent",
    "Topic :: Scientific/Engineering :: Atmospheric Science",
]

setup(
    name="pavics_sdi",
    version="0.1",
    url="https://pavics-sdi.readthedocs.io",
    install_requires=[],
    extras_require={
        "docs": [
            "sphinx>=1.4",
            "sphinx-intl",
            "sphinx_rtd_theme",
            "sphinx-jsondomain",  # unmaintained and has sphinx <2.0 hardcoded in dependencies
            "sphinx-jsonschema",
            "nbsphinx",
            "jinja2",
            "jupyter",
        ]
    },
    author="CRIM/Ouranos",
    author_email="pavics@ouranos.ca",
    description="Scientific gateway for climate data analytics.",
    long_description=open("README.rst", "rt").read(),
    license="BSD",
    classifiers=CLASSIFIERS,
)
