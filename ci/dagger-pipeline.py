"""Run notebook tests within a docker pipeline to test integration."""

import logging
import os
import sys
from pathlib import Path

try:
    import anyio
    import dagger
    from dagger import BuildArg
    from dagger.engine._version import CLI_VERSION as __dagger_version__  # noqa
except ImportError:
    raise ImportError(
        "Dagger is not installed. Please install it with `pip install dagger-io` first."
    )


BASE_IMAGE_TAG = os.getenv("BASE_IMAGE_TAG", "latest")
PAVICS_HOST_URL = os.getenv("PAVICS_HOST_URL", "https://pavics.ouranos.ca")
SANITIZE_FILE_URL = os.getenv(
    "SANITIZE_FILE_URL",
    "https://github.com/Ouranosinc/PAVICS-e2e-workflow-tests/raw/master/notebooks/output-sanitize.cfg",
)


async def main():
    async with dagger.Connection(
        dagger.Config(
            log_output=sys.stderr, workdir=Path(__file__).parent.parent.as_posix()
        )
    ) as client:
        sources = await (
            # pull container
            client.container().from_(f"pavics/workflow-tests:{BASE_IMAGE_TAG}")
            # copy files to container
            .with_directory(
                "/code", client.host().directory(".", exclude=[".git", "ci"])
            )
        )

        # run notebooks
        notebooks = (
            sources.with_exec(notebook_sanitizer("/code/docs/source/notebooks"))
            .with_env_variable("PAVICS_HOST_URL", PAVICS_HOST_URL)
            .with_exec(test_notebooks("/code/docs/source/notebooks"))
        )

        # execute
        whoami = await sources.with_exec(["whoami"]).stdout()
        version = await sources.with_exec(["python", "-V"]).stdout()
        whereami = await sources.with_exec(["pwd"]).stdout()
        whatshere = await sources.with_exec(["ls", "-alh"]).stdout()
        notebook_tests = await notebooks.stdout()

    print("\n")
    print(
        f"Hello from Dagger {__dagger_version__}"
        " and "
        f"{'.'.join([str(v) for v in sys.version_info[0:3]])}"
        " in "
        f"{whereami.strip()}\n"
        f"{whatshere.strip()}\n"
    )
    print(f"Running commands as `{whoami.strip()}` user in {version.strip()}.\n")
    print(notebook_tests)


def notebook_sanitizer(notebook_path: str) -> list[str]:
    logging.debug("Copying notebook output sanitizer ...")

    cmd = [
        "sh",
        "-c",
        "curl",
        "-L",
        SANITIZE_FILE_URL,
        "-o",
        f"{notebook_path}/output-sanitize.cfg",
        "--silent",
    ]
    return cmd


def test_notebooks(notebook_path: str) -> list[str]:
    logging.debug("Running notebook-based tests ...")

    cmd = [
        "pytest",
        "--nbval",
        "--verbose",
        notebook_path,
        "--nbval-sanitize-with",
        f"{SANITIZE_FILE_URL}/output-sanitize.cfg",
        "--ignore",
        f"{notebook_path}/.ipynb_checkpoints",
    ]
    return cmd


anyio.run(main)
