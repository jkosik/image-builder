#!/usr/bin/env python3
import boto3, time, json, os

# e.g.: us-east-1
region = os.environ['region']
# e.g.: ops
cmd_env = os.environ['cmd_env']

# e.g. luna-multi-tenant-ops
cluster_name = "luna-multi-tenant-" + cmd_env

client = boto3.client('ec2',region_name=region)
describe_res = client.describe_instances(
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

#print(describe_res)

print(f"List of VMs to reboot:")
for reservation in describe_res['Reservations']:
    for instance in reservation['Instances']:
        print(f"{instance['InstanceId']} - {instance['PrivateDnsName']}")

for reservation in describe_res['Reservations']:
    for instance in reservation['Instances']:
        print(f"Rebooting {instance['InstanceId']} and sleeping 10 mins")
        #sleep 10 mins (600s)
        # delete_res = client.reboot_instances(
        #     InstanceIds=[instance['InstanceId']]
        # )
        # time.sleep(600)

# test machine
# instance_id = 'i-0b14f668064f9c73d'


