#!/usr/bin/node
/*
 * prints My number:
 * <first argument converted in integer>
 * if the first argument can be converted to an integer:
 */

const argument = process.argv.slice(2);

if (argument.length === 1) {
  const num = argument[0];
  if (!isNaN(parseInt(num))) {
    console.log('My nymber: '+parseInt(argument[0]));
  } else { console.log('Not a number'); }
} else if (argument.length === 0) {
  console.log('Not a number');
}
