# local build and push to DockerHub

systemctl start docker
docker login
docker build -t jkosik/gcp-deployer:1.20.5 .
docker push jkosik/gcp-deployer:1.20.5
