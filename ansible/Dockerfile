FROM debian:stable-slim

ENV ANSIBLE_VERSION=4.2.0

ENV ANSIBLE_GATHERING=smart
ENV ANSIBLE_HOST_KEY_CHECKING=False
ENV ANSIBLE_SSH_PIPELINING=True

RUN apt-get update && apt-get upgrade -y && apt-get install -y \
    bash \
    curl \
    git \
    openssh-client \
    python3-pip \
&& rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache-dir \
                     ansible==$ANSIBLE_VERSION \
                     ansible-lint \
                     jmespath \
                     pyyaml

#RUN ansible-galaxy collection install community.kubernetes