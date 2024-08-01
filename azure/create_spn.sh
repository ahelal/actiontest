#!/bin/bash
set -euo nounset

echo "Creating a new service principal for RBAC in $subscriptionID:$resourceGroup"

let "randomIdentifier=$RANDOM*$RANDOM"
servicePrincipalName="bender-test-$randomIdentifier"
roleName="contributor"
subscriptionID=$(az account show --query id --output tsv)
# Verify the ID of the active subscription
echo "Using subscription ID $subscriptionID"

echo "Creating SP for RBAC with name $servicePrincipalName, with role $roleName and in scopes /subscriptions/$subscriptionID/resourceGroups/$resourceGroup"
az ad sp create-for-rbac --name $servicePrincipalName \
                         --role $roleName \
                         --scopes /subscriptions/$subscriptionID/resourceGroups/$resourceGroup \
                         --json-auth