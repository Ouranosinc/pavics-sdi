"""Build the documentation within a docker pipeline to test integration and notebooks."""

import sys
from pathlib import Path

try:
    import anyio
    import dagger
except ImportError:
    raise ImportError(
        "Dagger is not installed. Please install it with `pip install dagger-io` first."
    )


async def main():
    async with dagger.Connection(dagger.Config(log_output=sys.stderr)) as client:
        top_level_dir = client.host().directory(Path(__file__).parent.parent.as_posix())

        image_ref = await top_level_dir.docker_build()

        sources = (
            client.container()
            # pull container
            .from_("localpavics-sdi:latest").with_workdir("/code")
        )

        username = sources.with_exec(["whoami"])
        whats_here = sources.with_exec(["ls", "-la", "/code"])
        python_version = sources.with_exec(["python", "-V"])
        docs = sources.with_exec(["make", "--directory=/code/docs", "html"])

        # execute
        user = await username.stdout()
        contents = await whats_here.stdout()
        version = await python_version.stdout()
        docs_built = await docs.stdout()

    print(user)
    print(contents)

    print(f"Hello from Dagger and {version}")
    print(docs_built)


anyio.run(main)
