ARG CLOUD_SDK_VERSION=346.0.0

FROM gcr.io/google.com/cloudsdktool/cloud-sdk:${CLOUD_SDK_VERSION}-alpine

ENV KUBECTL_VERSION=v1.20.5

RUN apk --update --no-cache add  \
    bash \
    bind-tools \
    curl \
    jq \
    openssh-client

RUN curl -Lo /usr/local/bin/kubectl \
	https://storage.googleapis.com/kubernetes-release/release/${KUBECTL_VERSION}/bin/linux/amd64/kubectl \
	&& chmod +x /usr/local/bin/kubectl

RUN rm -rf /var/cache/apk/*  
