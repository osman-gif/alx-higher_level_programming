#!/usr/bin/node
/*
 * prints the first argument passed to it
 */

const argument = process.argv.slice(2);

if (!argument[0]) {
  console.log('No argument');
} else {
  console.log(argument[0]);
}
