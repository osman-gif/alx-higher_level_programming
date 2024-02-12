#!/usr/bin/node

/*
 * searches the second biggest integer in the list of arguments.
 */

const arg = process.argv.slice(2);

if (arg.length === 0 || arg.length === 1) {
  console.log(0);
} else {
  let fBig = parseInt(arg[0]);
  let sBig = parseInt(arg[1]);

  for (let i = 0; i < arg.length; i++) {
    if (fBig < arg[i]) {
      fBig = arg[i];
    }
  }

  for (let i = 0; i < arg.length; i++) {
    if (sBig < arg[i] && !(arg[i] === fBig)) {
      sBig = arg[i];
    }
  }

  console.log(sBig);
}
