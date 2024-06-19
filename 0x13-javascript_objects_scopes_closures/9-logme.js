#!/usr/bin/node

/*
 * Write a function that prints the number of arguments
 * already printed and the new argument value
 */

let printNum = 0;

exports.logMe = function (item) {
  console.log(printNum + ': ' + item);
  printNum++;
};
