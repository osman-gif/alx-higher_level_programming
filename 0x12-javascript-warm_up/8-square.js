#!/usr/bin/node
/*
 * 8-square.js
 */

const arg = process.argv.slice(2);
const size = arg[0];

if (!isNaN(size) && parseInt(size)) {
  for (let i = 0; i < (size); i++) {
    let str = '';
    for (let j = 0; j < (size); j++) {
      str += 'x';
    }
    console.log(str);
  }
} else {
  console.log('Missing size');
}
