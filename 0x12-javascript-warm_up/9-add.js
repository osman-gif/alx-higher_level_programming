#!/usr/bin/node

/*
 * prints the addition of 2 integers
 */

const arg = process.argv.slice(2);

const fNum = arg[0];
const sNum = arg[1];

function add (a, b) {
  console.log(parseInt(a) + parseInt(b));
}

add(fNum, sNum);
