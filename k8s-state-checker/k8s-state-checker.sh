#!/bin/bash

kubectl get po -l app!=k8s-state-checker --no-headers > pods
helm list > helm-charts

kubectl create cm expected-versions --from-file=pods --from-file=charts
sleep 5

kubectl describe cm expected-versions

echo "=== MD5 Hash of the expected-version ConfigMap (kubectl get cm expected-versions -o yaml) ==="
kubectl get cm expected-versions -o yaml | md5sum

