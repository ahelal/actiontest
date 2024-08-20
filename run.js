// import { context } from '@actions/github'
context = require('@actions/github');
// print all env variables to console


console.log("_____ Printing all environment variables _____");
// Iterate over all environment variables and print them to the console
for (const [key, value] of Object.entries(process.env)) {
    console.log(`) ${key}: ${value}`);
}
console.log("_____                                      _____");


console.log('Context = ', JSON.stringify(context, null, 2));