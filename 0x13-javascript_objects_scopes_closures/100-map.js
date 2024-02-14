#!/usr/bin/node

/*
 * imports an array and computes a new array.
 */

const list = require('./100-data.js').list;

const result = list.map((n, idx) => n * idx);
console.log(result);
