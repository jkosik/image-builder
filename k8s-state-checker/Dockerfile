FROM bullseye-slim

ENV KUBECTL_VERSION=v1.20.5

# basic binaries
RUN apt update && apt-get upgrade -y && apt install -y \
    bash \
    jq \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY k8s-state-checker.sh .

# kubectl
RUN curl -Lo /usr/local/bin/kubectl \
	https://storage.googleapis.com/kubernetes-release/release/${KUBECTL_VERSION}/bin/linux/amd64/kubectl \
	&& chmod +x /usr/local/bin/kubectl


# install helm
RUN curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 \
    && chmod 700 get_helm.sh \
    && ./get_helm.sh

RUN ["chmod", "+x", "./entrypoint.sh"]
ENTRYPOINT ["./entrypoint.sh"]
