# GitHub Actions build and push to DockerHub
1. Create `Dockerfile` in the Folder matching the future Image (and GitHub Repository) name.
2. Create Workflow file in `/.github`
3. Parametrize global ENVs in the Workflow file to match values from `Dockerfile`. Keep both files in sync when updating images.
4. Update also trigger `on.push.paths` - can not be directly parametrized yet.

# Local build and push to DockerHub
```
systemctl start docker
docker login
docker build -t jkosik/gcp-deployer:346 .
docker push jkosik/gcp-deployer:346
```