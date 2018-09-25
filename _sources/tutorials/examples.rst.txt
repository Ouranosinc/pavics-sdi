Preliminary bit of code::

    from owslib.wps import WebProcessingService
    pavics = 'https://pavics.ouranos.ca/twitcher/ows/proxy/flyingpigeon'
    headers = credentials()
    wps = WebProcessingService(pavics, headers=headers, verify=False)


Bias correction
---------------

Using a bias correction algorithm from the console::

    inputs = [('obs':'Enter observation dataset' ), ('ref': 'Enter reference simulated dataset'), ('fut': 'Enter future simulated dataset')]
    wps.execute('kddm_bc', inputs, output='output_netcdf_fut')



Climate indices
---------------

Compute climate indices from a simulated time series::

    inputs = [('resource':), ]
    wps.execute('icclim_TXx', inputs, output='output_netcdf')



Spatial subsetting
------------------

Extract a portion of a netCDF file over a country::

    inputs = [('region': 'CAN'), ('resource': '')]
    wps.execute('subset_countries', inputs, output='ncout')


Average over a polygon served through WFS::

    inputs = [('resource':''), ('typename':''), ('featureids':'')]
    wps.execute('averager_WFS', inputs, output='output')


Note that in this last case, the process returns a JSON file storing the URL of the output file, rather than returning
the file itself. This is an alternative pattern we are experimenting with to facilitate the handling of multifile outputs.