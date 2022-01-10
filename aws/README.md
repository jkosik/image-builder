# Test locally
```
docker build -t aws .
docker run -ti -e AWS_ACCESS_KEY_ID='YOUR_AWS_ID' -e AWS_SECRET_ACCESS_KEY='YOUR_AWS_KEY' aws aws --version
docker run -ti -e AWS_ACCESS_KEY_ID='YOUR_AWS_ID' -e AWS_SECRET_ACCESS_KEY='YOUR_AWS_KEY' -e cmd_env='ops' -e region='us-east-1' aws python reboot-ec2.py
```

# Sample manifest
```
---
apiVersion: v1
kind: Secret
metadata:
  name: cmd-ops-creds
stringData:
  aws_access_key_id: "YOUR_AWS_ID"
  aws_secret_access_key: "YOUR_AWS_KEY"

---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: reboot-ec2
  labels:
    app: reboot-ec2
spec:
  replicas: 1
  selector:
    matchLabels:
      app: reboot-ec2
  template:
    metadata:
      labels:
        app: reboot-ec2
    spec:
      containers:
      - name: reboot-ec2
        image: jkosik/aws:latest
        env:
          - name: cmd_env
            value: ops
          - name: region
            value: us-east-1
        envFrom:
          - secretRef:
              name: cmd-ops-creds
        args: ["python3", "reboot-ec2.py"]
```