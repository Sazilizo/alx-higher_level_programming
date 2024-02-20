#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

function getResponse (err, data) {
  if (err) {
    console.error(err);
  } else {
    console.log('code: ' + data.statusCode);
  }
}
request(url, getResponse);
