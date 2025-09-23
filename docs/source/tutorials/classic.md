---
file_format: mystnb
---

# Running CLASSIC

The PAVICS environment includes librairies and tools to compile and run [CLASSIC](https://cccma.gitlab.io/classic_pages/).

```{note}
Note that as of September 2023, these tools are only available in the `alpha` environment. To switch environment, go the File -> Hub Control Panel, and click on Stop My Server, then select the `alpha` environment from the dropdown menu and click on Start My Server.
```


## Installation

1. In the JupyterLab interface, go into the File Browser sidebar and navigate to your writable-workspace folder.
2. Open the Git sidebar clone the ClASSIC repository, and click on ``Clone a Repository``.
3. Enter the URL of the CLASSIC repository: `https://gitlab.com/cccma/classic` and press Enter. You should now see a new folder named `classic` in your workspace, click on it.
4. Open a terminal by clicking on File -> New Launcher then clicking on the ``Terminal`` icon. Enter ``pwd`` to confirm you are in the folder `/notebook_dir/writable-workspace/classic`
5. Run ``make`` to compile CLASSIC. Once the compilation is done (it will take a few minutes), you'll find the executable in ``bin/CLASSIC_serial``.

You're welcome to contribute instructions to compile the parallel version.

## Running CLASSIC with CRCM data
TODO

## Running CLASSIC with ERA5 data
TODO

## Running CLASSIC with CaSR data
TODO

## Running CLASSIC with ECCC station data
TODO
