

param storageAccountName string = 'staccnmadsfi672345hsd'

// resource rg 'Microsoft.Resources/resourceGroups@2021-04-01' existing = {
//   name: resourceGroupName
// }

module stacc 'storageAccount.bicep' = [for i in range(0, 1): {
  name: 'stacc_${i}'
  scope: resourceGroup()
  params: {
    storageAccountName: storageAccountName
  }
}]
