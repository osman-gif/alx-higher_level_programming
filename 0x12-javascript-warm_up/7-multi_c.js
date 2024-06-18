#!/usr/bin/node
/*
 *  prints x times C is fun'
 */

const argument = process.argv.slice(2);
const num = argument[0];

if (argument.length === 1 && !isNaN(parseInt(num))) {
  let count = 0;
  while (count < num) {
    console.log('C is fun');
    count++;
  }
} else if (argument.length === 0 || isNaN(parseInt(num))) {
  console.log('Missing number of occurrences');
}
