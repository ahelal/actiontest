#!/usr/bin/env python3

from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient
import paramiko
import os


credential = DefaultAzureCredential()
subscription_id = os.environ.get('AZURE_SUBSCRIPTION_ID')
resource_group_name = "bender_tests"
location = "eastus"
compute_client = ComputeManagementClient(credential, subscription_id)
ssh_key_name = 'your_ssh_key_name'

# create a directory if it doesn't exist ssh_temp in this script path 
if not os.path.exists('ssh_temp'):
    os.makedirs('ssh_temp')

key = paramiko.RSAKey.generate(2048)
private_key_path = os.path.expanduser('ssh_temp/id_rsa')
public_key_path = os.path.expanduser('ssh_temp/id_rsa.pub')

# Save private key
with open(private_key_path, 'w') as private_key_file:
    key.write_private_key(private_key_file)

# Save public key
with open(public_key_path, 'w') as public_key_file:
    public_key_file.write(f"{key.get_name()} {key.get_base64()}")

ssh_key_parameters = {
    'location': location,
    'public_key': open(public_key_path).read()
}

compute_client.ssh_public_keys.create(
    resource_group_name=resource_group_name,
    ssh_public_key_name=ssh_key_name,
    parameters=ssh_key_parameters
)

print("SSH key created and stored in Azure successfully.")