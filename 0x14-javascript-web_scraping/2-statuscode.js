#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  !error ? console.log('code:', response.statusCode) : console.error(error);
});
