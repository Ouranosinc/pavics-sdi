"""Build the documentation within a docker pipeline to test integration and notebooks."""

import os
import sys
from pathlib import Path

try:
    import anyio
    import dagger
    from dagger import BuildArg
except ImportError:
    raise ImportError(
        "Dagger is not installed. Please install it with `pip install dagger-io` first."
    )


async def main():
    async with dagger.Connection(dagger.Config(log_output=sys.stderr)) as client:
        top_level_dir = client.host().directory(Path(__file__).parent.parent.as_posix())

        # build container
        sources = await top_level_dir.docker_build(
            build_args=BuildArg("BASE_IMAGE_TAG", os.getenv("BASE_IMAGE_TAG"))
            if os.getenv("BASE_IMAGE_TAG")
            else None,
        )

        # smoke tests
        python_version = sources.with_exec(["python", "-V"])
        username = sources.with_exec(["whoami"])

        # build docs
        docs = sources.with_exec(["make", "--directory=/code/docs", "html"])

        # execute
        user = await username.stdout()
        version = await python_version.stdout()
        docs_built = await docs.stdout()

    print(f"Hello from Dagger and {version}")
    print(f"Running commands as {user} user.")

    print(docs_built)


anyio.run(main)
