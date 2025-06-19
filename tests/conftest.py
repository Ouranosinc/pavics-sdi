"""Pytest configuration file."""


def pytest_collectstart(collector):
    # Make sure ancestor folder name do not end with `.ipynb`, else we have
    # AttributeError: 'Session' object has no attribute 'skip_compare'.
    if collector.fspath and collector.fspath.ext == ".ipynb":
        collector.skip_compare += (
            "text/html",
            "application/javascript",
            "application/vnd.holoviews_load.v0+json",
        )
