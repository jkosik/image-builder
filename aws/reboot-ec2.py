#!/usr/bin/env python3
import boto3, time, json, os

# e.g.: us-east-1
region = os.environ['region']
# e.g.: ops
cmd_env = os.environ['cmd_env']

# e.g. luna-multi-tenant-ops
cluster_name = "luna-multi-tenant-" + cmd_env

client = boto3.client('ec2',region_name=region)
response = client.describe_instances(
  Filters=[
        {
            'Name': 'tag:eksctl.cluster.k8s.io/v1alpha1/cluster-name',
            'Values': [cluster_name],
        },
        {
            'Name': 'tag:alpha.eksctl.io/nodegroup-name',
            'Values': [
                'eks-worker-default-1-18-amazon2-use1a-v3',
                'eks-worker-xlarge-1-18-amazon2-use1a-v3'
            ]
        },        
  ],
)

#print(response)

print(f"List of VMs to reboot:")
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print(f"{instance['InstanceId']} - {instance['PrivateDnsName']}")

# for reservation in response['Reservations']:
#     for instance in reservation['Instances']:
#         print(f'Rebooting {instance['InstanceId']} and sleeping 10 mins')
#         #sleep 10 mins (600s)
#         instance = ec2.Instance(instance['InstanceId'])
#         instance.reboot()
#         time.sleep(600)

# test machine
# instance_id = 'i-0b14f668064f9c73d'

# ec2 = boto3.resource(
#       'ec2', 
#     #   aws_access_key_id='xxx',
#     #   aws_secret_access_key='xxx',
#       region_name=region     
#       )
# instance = ec2.Instance(instance_id)
# instance.reboot()
# print(f'EC2 instance "{instance.id}" has been rebooted')

