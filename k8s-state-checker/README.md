# K8S State Checker
Image runs set of `kubectl` and `helm` commands against Kubernetes API and stores outcome to a ConfigMap.

## Run
Run by deploying the following manifest
```
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: k8s-state-checker
  labels:
    app: k8s-state-checker
spec:
  replicas: 1
  selector:
    matchLabels:
      app: k8s-state-checker
  template:
    metadata:
      labels:
        app: k8s-state-checker
    spec:
      containers:
      - name: k8s-state-checker
        image: jkosik/k8s-state-checker
```