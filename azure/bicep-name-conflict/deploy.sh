#!/usr/bin/env bash
resource_group="bender_test_rg"

az deployment group create \
    --resource-group "${resource_group}" \
    --template-file ./main.bicep \
    --name stacc_name-conflict_bicep-simple
