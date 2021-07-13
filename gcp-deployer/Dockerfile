ARG CLOUD_SDK_VERSION=346.0.0

FROM gcr.io/google.com/cloudsdktool/cloud-sdk:${CLOUD_SDK_VERSION}-slim

ENV KUBECTL_VERSION=v1.20.5
ENV TF_VERSION=1.0.1
ENV ANSIBLE_VERSION=4.2.0
ENV ANSIBLE_GATHERING=smart
ENV ANSIBLE_HOST_KEY_CHECKING=False
ENV ANSIBLE_SSH_PIPELINING=True


# sudo apt install python3.8
# add-apt-repository ppa:deadsnakes/ppa
# apt install python3.8

# basic binaries
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
    bash \
    curl \
    git \
    jq \
    openssh-client \
    python3.8 \
    python3-pip \
    software-properties-common \
    unzip \
&& rm -rf /var/lib/apt/lists/*

# kubectl
RUN curl -Lo /usr/local/bin/kubectl \
	https://storage.googleapis.com/kubernetes-release/release/${KUBECTL_VERSION}/bin/linux/amd64/kubectl \
	&& chmod +x /usr/local/bin/kubectl

# terraform
RUN curl --output terraform_${TF_VERSION}_linux_amd64.zip https://releases.hashicorp.com/terraform/${TF_VERSION}/terraform_${TF_VERSION}_linux_amd64.zip \
    && unzip terraform_${TF_VERSION}_linux_amd64.zip \
    && mv terraform /usr/local/bin/terraform-${TF_VERSION} \
    && ln -s /usr/local/bin/terraform-${TF_VERSION} /usr/local/bin/terraform \
    && rm terraform_${TF_VERSION}_linux_amd64.zip

# ansible
RUN pip3 install --no-cache-dir \
                     ansible==$ANSIBLE_VERSION \
                     ansible-lint \
                     jmespath

