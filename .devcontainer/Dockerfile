# Start with the base Ubuntu image
FROM ubuntu:22.04
# Add label maintainer
LABEL maintainer="gluonhiggs"

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
    apt install -y curl unzip

ARG SPARK_HOME=/usr/local/spark
ENV PATH="${SPARK_HOME}/bin:$PATH"

RUN wget https://downloads.apache.org/spark/spark-3.0.1/spark-3.0.1-bin-hadoop2.7.tgz &&\
    tar -xzf spark-3.0.1-bin-hadoop2.7.tgz &&\
    mv spark-3.0.1-bin-hadoop2.7 spark



# Create a directory for our application
RUN mkdir /workspaces
WORKDIR /workspaces
COPY . /workspaces

#  Update pip
RUN python3 -m pip install --upgrade pip

RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64-2.0.30.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    ./aws/install
    
# ENV REFRESHED_AT 2023-01-06

# Install Python packages specified in requirements.txt
RUN python3 -m pip install -r ./.devcontainer/requirements.txt

# Make port 8888 available to the world outside this container
EXPOSE 8888
CMD ["java", "--version"]