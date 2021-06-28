# GitHub Actions build and push to DockerHub
1. Create `Dockerfile` in the Folder matching the Image (and GitHub Repository) name.
2. Create Workflow file in `/.github`
3. Parametrize global ENVs in the Workflow file to match values from `Dockerfile`.
4. Update trigger (on.push.paths) - can not be directly parametrized yet.

Optionally use ARG instead of ENV in the `Dockerfile` and use build extra args for the image build in the respective GitHub Action. No need to update Dockerfiles anymore. Issue might popup

# Local build and push to DockerHub
```
systemctl start docker
docker login
docker build -t jkosik/gcp-deployer:346 .
docker push jkosik/gcp-deployer:346
```