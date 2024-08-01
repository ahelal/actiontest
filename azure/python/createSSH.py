#!/usr/bin/env python3

import paramiko
import json
import os

from azure.identity import ClientSecretCredential, DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient


# Read from environment variables

azure_credentials = os.environ['AZURE_CREDENTIALS']

auth_data = json.load(azure_credentials)

client_id = auth_data['clientId']
client_secret = auth_data['clientSecret']
tenant_id = auth_data['tenantId']

# Create a ClientSecretCredential
credential = ClientSecretCredential(
    client_id=client_id,
    client_secret=client_secret,
    tenant_id=tenant_id
)

# Use the credential to authenticate the ComputeManagementClient
resource_group_name = "bender_test_rg"
location = "eastus"
compute_client = ComputeManagementClient(credential, subscription_id=auth_data['subscriptionId'])
ssh_key_name = 'test_ssh_key'

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