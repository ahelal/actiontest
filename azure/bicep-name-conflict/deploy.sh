#!/usr/bin/env bash
set -e
SCRIPT_DIR="$( cd "$( dirname "$0" )" && pwd)"
resource_group="bender_test_rg"

cd "${SCRIPT_DIR}"

az deployment group create \
    --resource-group "${resource_group}" \
    --template-file ./main.bicep \
    --name stacc_name-conflict_bicep-simple
