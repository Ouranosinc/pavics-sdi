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

