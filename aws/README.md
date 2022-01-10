# Test locally
```
docker build -t aws .
docker run -ti -e AWS_ACCESS_KEY_ID='YOUR_AWS_ID' -e AWS_SECRET_ACCESS_KEY='YOUR_AWS_KEY' aws aws --version
docker run -ti -e AWS_ACCESS_KEY_ID='YOUR_AWS_ID' -e AWS_SECRET_ACCESS_KEY='YOUR_AWS_KEY' -e cmd_env='ops' -e region='us-east-1' aws python reboot-ec2.py
```