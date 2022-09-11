FROM ubuntu:jammy-20220815

ENV TF_VERSION=1.2.9
#ENV ANSIBLE_VERSION=6.3.0
ENV ANSIBLE_CORE_VERSION=2.13.3

RUN apt update && apt upgrade -y && apt install -y \
    ansible-lint \
    bash \
    curl \
    git \
    jq \
    openssh-client \
    python3-pip \
    unzip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# TF
RUN curl --output terraform_${TF_VERSION}_linux_amd64.zip https://releases.hashicorp.com/terraform/${TF_VERSION}/terraform_${TF_VERSION}_linux_amd64.zip \
    && unzip terraform_${TF_VERSION}_linux_amd64.zip \
    && mv terraform /usr/local/bin/terraform-${TF_VERSION} \
    && ln -s /usr/local/bin/terraform-${TF_VERSION} /usr/local/bin/terraform \
    && rm terraform_${TF_VERSION}_linux_amd64.zip

# TF Linters
RUN curl -s https://raw.githubusercontent.com/terraform-linters/tflint/master/install_linux.sh | bash
RUN curl -s https://raw.githubusercontent.com/aquasecurity/tfsec/master/scripts/install_linux.sh | bash

# Ansible
RUN pip3 install ansible-core==${ANSIBLE_CORE_VERSION}
