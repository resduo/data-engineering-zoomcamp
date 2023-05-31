# Start with the base Ubuntu image
FROM ubuntu:22.04
# Add label maintainer
LABEL maintainer="gluonhiggs"

ARG JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV PATH="${JAVA_HOME}/bin:${PATH}"

# Install software-properties-common, and then Python 3.10 using APT repository
RUN apt update &&\
    apt install -y software-properties-common &&\
    # apt-get install -y curl unzip &&\
    apt install -y openjdk-11-jdk &&\
    apt update && \
    apt install ca-certificates-java -y && \
    apt clean && \
    update-ca-certificates -f
# # Use the output of "which java" to set JAVA_HOME
# RUN JAVA_HOME=$(whereis java) && echo $JAVA_HOME > /etc/environment

# # Add JAVA_HOME to PATH
# ENV PATH="${JAVA_HOME}/bin:${PATH}"

# Create a directory for our application
# RUN mkdir /workspaces
# WORKDIR /workspaces
# COPY . /workspaces

# #  Update pip
# RUN python3 -m pip install --upgrade pip

# RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64-2.0.30.zip" -o "awscliv2.zip" && \
#     unzip awscliv2.zip && \
#     ./aws/install
    
# ENV REFRESHED_AT 2023-01-06

# # Install Python packages specified in requirements.txt
# RUN python3 -m pip install -r ./.devcontainer/requirements.txt

# # Make port 8888 available to the world outside this container
# EXPOSE 8888
CMD ["java", "--version"]