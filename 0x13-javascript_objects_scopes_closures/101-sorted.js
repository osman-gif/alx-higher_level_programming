#!/usr/bin/node

/*
 * imports a dictionary of occurrences by user id
 * and computes a dictionary of user ids by occurrence.
 */

const dict = require('./101-data.js').dict;

const list = dict.enum();


console.log(list);
