#!/usr/bin/node

const { argv } = require('node:process');
const num = 0;

if (typeof +argv[2] === typeof num) {
  console.log(`My number: ${argv[2]}`);
} else {
  console.log('Not a number');
}
