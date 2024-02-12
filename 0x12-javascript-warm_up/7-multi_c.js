#!/usr/bin/node
/*
 *  prints x times C is fun'
 */

const argument = process.argv.slice(2);

if (argument.length === 1) {
  const num = argument[0];

  if (!isNaN(parseInt(num))) {
    let count = 0;
    while (count < num) {
      console.log('C is fun');
      count++;
    }
  } else { console.log('Missing number of occurrences'); }
} else if (argument.length === 0) {
  console.log('Missing number of occurrences');
}
