# Use builder pattern to build the image
# https://docs.docker.com/develop/develop-images/multistage-build/
# https://docs.docker.com/develop/develop-images/dockerfile_best-practices/
# Get based image
FROM ubuntu:22.04 AS builder

# Add label maintainer
LABEL maintainer="gluonhiggs"

# Create a directory for our application
WORKDIR /workspaces
COPY . /workspaces

# Set environment variables for Java

ARG JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV PATH="${JAVA_HOME}/bin:$PATH"

# Install software-properties-common, and then Python 3.10 using APT repository
RUN apt update &&\
    apt install -y software-properties-common &&\
    add-apt-repository ppa:deadsnakes/ppa &&\
    apt install -y openjdk-11-jdk-headless &&\
    apt update && \
    apt install ca-certificates-java -y && \
    apt clean && \
    update-ca-certificates -f

# Python installation
RUN apt install -y python3.10 python3-pip python3.10-dev &&\
    apt install -y curl unzip wget

# Set environment variables for Spark
ARG SPARK_HOME=/usr/local/spark
ENV PATH="${SPARK_HOME}/bin:$PATH"

ENV SPARK_VERSION=3.0.2 \
HADOOP_VERSION=3.2 \
SPARK_HOME=/opt/spark \
PYTHONHASHSEED=1

# Download and uncompress spark from the apache archive
RUN wget --no-verbose -O apache-spark.tgz "https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz" \
&& mkdir -p /opt/spark \
&& tar -xf apache-spark.tgz -C /opt/spark --strip-components=1 \
&& rm apache-spark.tgz

# Update pip
RUN python3 -m pip install --upgrade pip

# Install AWS CLI
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64-2.0.30.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    ./aws/install
    
# ENV REFRESHED_AT 2023-01-06

# Install Python packages specified in requirements.txt
RUN python3 -m pip install -r ./.devcontainer/requirements.txt

# Keeping only the app in the image
FROM ubuntu:22.04
WORKDIR /workspaces
COPY --from=builder /workspaces /workspaces

# Make port 8888 available to the world outside this container
EXPOSE 8888



