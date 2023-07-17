# vim:set ft=dockerfile:
ARG BASE_IMAGE_TAG
FROM pavics/workflow-tests:${BASE_IMAGE_TAG:-latest}
ARG DEBIAN_FRONTEND=noninteractive
ENV PIP_ROOT_USER_ACTION=ignore
LABEL org.opencontainers.image.authors="https://github.com/ouranosinc/pavics-sdi"
LABEL Description="PAVICS-SDI-TESTING-IMAGE" Vendor="Birdhouse" Version="1.3.0"

# root-level commands
USER root

# Install build tools
RUN apt-get install --yes build-essential

# Switch to /code directory
WORKDIR /code

# Build finch environment
COPY environment-dev.yml /code
RUN mamba install -n birdy python=3.8 --yes \
    && mamba env update -n birdy -f environment-dev.yml \
    && mamba clean --all --yes

# Add the finch conda environment to the path
ENV PATH /opt/conda/envs/birdy/bin:$PATH

# Copy finch source code
COPY . /code

# Build the documentation
CMD ["make", "--directory=/code/docs", "html"]
