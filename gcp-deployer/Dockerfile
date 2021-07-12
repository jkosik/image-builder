ARG CLOUD_SDK_VERSION=346.0.0

FROM gcr.io/google.com/cloudsdktool/cloud-sdk:${CLOUD_SDK_VERSION}-slim

ENV KUBECTL_VERSION=v1.20.5

RUN apt-get update && apt-get upgrade -y && apt-get install -y \
    bash \
    bind-tools \
    curl \
    jq \
    openssh-client
&& rm -rf /var/lib/apt/lists/*

RUN curl -Lo /usr/local/bin/kubectl \
	https://storage.googleapis.com/kubernetes-release/release/${KUBECTL_VERSION}/bin/linux/amd64/kubectl \
	&& chmod +x /usr/local/bin/kubectl
