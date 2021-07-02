FROM python:3.9-slim

ENV TF_VERSION=1.0.1

# RUN apk add --update --no-cache curl \
#         bash \
#         curl \
#         git \
#         jq \
#         openssh-client \

RUN apt-get update && apt-get upgrade -y && apt-get install -y \
    bash \
    curl \
    git \
    jq \
    openssh-client \
&& rm -rf /var/lib/apt/lists/*

RUN curl --output terraform_${TF_VERSION}_linux_amd64.zip https://releases.hashicorp.com/terraform/${TF_VERSION}/terraform_${TF_VERSION}_linux_amd64.zip \
    && unzip terraform_${TF_VERSION}_linux_amd64.zip \
    && mv terraform /usr/local/bin/terraform-${TF_VERSION} \
    && ln -s /usr/local/bin/terraform-${TF_VERSION} /usr/local/bin/terraform \
    && rm terraform_${TF_VERSION}_linux_amd64.zip

