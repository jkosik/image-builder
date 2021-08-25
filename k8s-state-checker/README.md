# K8S State Checker
Image runs set of `kubectl` and `helm` commands against Kubernetes API and stores outcome to a ConfigMap `expected-versions`.

## Run
```
kubectl apply -f deployment.yaml
```

Multiple K8S resources are created and MD5 Hash is calculated from `expected-version` ConfigMap.
See:
```
kubectl logs PODNAME
```

## Deployment
Include `deployment.yaml` to the Helm Charts deployed on the target cluster and hook control script against the newly created ConfigMap.

## Notes
ConfigMap is not deleted when running `kubectl delete -f deployment.yaml` so repetitive run fails.
