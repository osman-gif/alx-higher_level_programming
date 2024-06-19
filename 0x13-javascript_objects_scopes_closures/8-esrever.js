#!/usr/bin/node

/*
 * returns the reversed version of a list
 */

exports.esrever = function (list) {
  const len = list.length;
  const revList = [];

  for (let i = len - 1; i >= 0; i--) {
    revList.push(list[i]);
  }

  return revList;
};
