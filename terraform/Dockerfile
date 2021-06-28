FROM alpine

ENV TF_VERSION=1.0.1

# Tools
RUN apk add --update --no-cache curl \
                                 git \
                                 jq \
                                 openssh-client \
                                 openssh-keygen \
                                 wget 

# Terraform
RUN curl --output terraform_${TF_VERSION}_linux_amd64.zip https://releases.hashicorp.com/terraform/${TF_VERSION}/terraform_${TF_VERSION}_linux_amd64.zip \
    && unzip terraform_${TF_VERSION}_linux_amd64.zip \
    && mv terraform /usr/local/bin/terraform-${TF_VERSION} \
    && ln -s /usr/local/bin/terraform-${TF_VERSION} /usr/local/bin/terraform \
    && rm terraform_${TF_VERSION}_linux_amd64.zip

