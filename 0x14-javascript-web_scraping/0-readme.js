#!/usr/bin/node
const fs = require('fs');
const file = process.argv[2];
const format = 'utf8';
fs.readFile(file, format, function (err, data) {
  if (err != null) {
    return console.log(err);
  }
  console.log(data);
});
