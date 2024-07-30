#!/usr/bin/node

const fs = require('fs');
const file = process.argv[2];
const format = 'utf8';
const string = process.argv[3];

fs.writeFile(file, string, format, function (err) {
  if (err) { return console.log(err); }
});
