ARG CLOUD_SDK_VERSION=346.0.0

FROM gcr.io/google.com/cloudsdktool/cloud-sdk:${CLOUD_SDK_VERSION}-slim

ENV KUBECTL_VERSION=v1.20.5
ENV ANSIBLE_VERSION=4.2.0
ENV ANSIBLE_GATHERING=smart
ENV ANSIBLE_HOST_KEY_CHECKING=False
ENV ANSIBLE_SSH_PIPELINING=True

RUN apt-get update && apt-get upgrade -y && apt-get install -y \
    bash \
    curl \
    git \
    jq \
    openssh-client \
    python3-pip \
&& rm -rf /var/lib/apt/lists/*

RUN curl -Lo /usr/local/bin/kubectl \
	https://storage.googleapis.com/kubernetes-release/release/${KUBECTL_VERSION}/bin/linux/amd64/kubectl \
	&& chmod +x /usr/local/bin/kubectl

RUN pip3 install --no-cache-dir \
                     ansible==$ANSIBLE_VERSION \
                     ansible-lint \
                     jmespath

