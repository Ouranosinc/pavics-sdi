===============================================
Working with Web Processing Service with python
===============================================

Basic WPS interaction using OWSLib is described in their documentation:
https://geopython.github.io/OWSLib/#wps

Currently, we recommend the following branch of owslib since it allows
for the distinction between sync/async execution:
https://github.com/bird-house/OWSLib/tree/pingudev::

    pip install --upgrade --force-reinstall https://github.com/bird-house/OWSLib/archive/pingudev.zip)

Getting a list of processes::

    from owslib.wps import WebProcessingService
    wps = WebProcessingService('http://localhost:8081/pywps')
    wps.getcapabilities()
    processes = [x.identifier for x in wps.processes]

Inputs identifers::

    process = wps.describeprocess('some_process')
    inputs = [x.identifier for x in process.dataInputs]

Execute process (synchronous)::

    myinputs = [('some_parameter', 'some_value')]
    execution = wps.execute('some_process', myinputs, async=False)
    execution.getStatus()
    execution.statusLocation  # useful for accessing the xml status file
    execution.processOutputs[0].data

Execute process with file inputs/outputs (asynchronous)::

    from owslib.wps import ComplexDataInput
    myinputs = [
        ('some_file_input', ComplexDataInput('http://localhost/file.nc')),
        ('some_string_parameter', 'some_value'),
    ]
    execution = wps.execute('some_process', myinputs, output='OUTPUT')
    while execution.status != 'ProcessSucceeded':
        execution.checkStatus(sleepSecs=1)
        if execution.status == 'ProcessFailed':
            break
    execution.processOutputs[0].reference

On a local flyingpigeon, the results can also be found in::

    ~/birdhouse/var/lib/pywps/outputs/

If the WPS is protected behind magpie::

    import requests
    credentials = dict(provider_name='ziggurat',
                       user_name='magpie_username',
                       password='magpie_password')
    s = requests.Session()
    response = s.post('{0}/signin'.format(https://localhost/magpie), data=credentials, verify=False)
    auth_tkt = response.cookies.get('auth_tkt', domain='localhost.local')
    headers = dict(Cookie='auth_tkt={0}'.format(auth_tkt))
    wps = WebProcessingService('https://localhost/twitcher/ows/proxy/wpsandbox/pywps', headers=headers, verify=False)
