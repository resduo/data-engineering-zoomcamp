# Start with the base Ubuntu image
FROM ubuntu:22.04
# Add label maintainer
LABEL maintainer="gluonhiggs"


# Install software-properties-common, and then Python 3.10 using APT repository
RUN apt-get update &&\
    apt-get install -y software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update &&\
    apt-get install -y python3.10 python3.10-distutils python3.10-venv python3.10-dev&& \
    apt-get install -y curl openjdk-11-jdk

ENV LC_ALL C

# # Install required pip packages including pyspark from requirements.txt
RUN mkdir /workspaces
WORKDIR /workspaces
COPY . /workspaces


RUN curl https://bootstrap.pypa.io/get-pip.py | python3 && \
    pip3 install --upgrade pip

# Copy all files in the current directory on the host machine
# to the /workspaces/ directory in the Docker image

# Install Python packages specified in requirements.txt
RUN python3 -m pip install -r ./.devcontainer/requirements.txt

# Make port 8888 available to the world outside this container
EXPOSE 8888
