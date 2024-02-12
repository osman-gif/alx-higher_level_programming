#!/usr/bin/node
/*
 * This script prints a message depending of the number of arguments passed
 */

const argument = process.argv.slice(2);

const arg1 = argument[0];
const arg2 = argument[1];
console.log(arg1 + ' is ' + arg2);
