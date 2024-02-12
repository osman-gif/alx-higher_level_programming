#!/usr/bin/node

/*
 * searches the second biggest integer in the list of arguments.
 */

const arg = process.argv.slice(2);

if (arg.length === 0 || arg.length === 1) {
  console.log(0);
} else {
  let fBig = 0;
  let sBig = 0;

  for (let i = 0; i < arg.length; i++) {
    if (fBig < parseInt(arg[i])) {
      fBig = parseInt(arg[i]);
    }
  }

  for (let i = 0; i < arg.length; i++) {
    if (sBig < parseInt(arg[i]) && !(parseInt(arg[i]) === fBig)) {
      sBig = parseInt(arg[i]);
    }
  }

  console.log(sBig);
}
