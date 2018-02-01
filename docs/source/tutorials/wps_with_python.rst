===============================================
Working with Web Processing Service with python
===============================================

Basic WPS interaction using OWSLib is described in their documentation:
https://geopython.github.io/OWSLib/#wps

Getting a list of processes::

    from owslib.wps import WebProcessingService
    wps = WebProcessingService('http://localhost:8081/pywps')
    wps.getcapabilities()
    processes = [x.identifier for x in wps.processes]

Inputs identifers::

    process = wps.describeprocess('some_process')
    inputs = [x.identifier for x in process.dataInputs]

Execute process (async)::

    myinputs = [('some_parameter', 'some_value')]
    execution = wps.execute('some_process', myinputs, async=False)
    execution.getStatus()
    execution.processOutputs[0].data

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
