#!/usr/bin/node

const fs = require('fs');
const request = require('request');
let url = process.argv[2];
request(url).pipe(fs.createWriteStream(process.argv[3]));
