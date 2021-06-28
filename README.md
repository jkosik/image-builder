# GitHub Actions build and push to DockerHub
1. Create workflow file
2. Parametrize global ENVs
3. Update trigger (on.push.paths) - can not be directly parametrized yet

# Local build and push to DockerHub
```
systemctl start docker
docker login
docker build -t jkosik/gcp-deployer:346 .
docker push jkosik/gcp-deployer:346
```