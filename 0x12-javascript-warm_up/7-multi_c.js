#!/usr/bin/node

const { argv } = require('node:process');

if (!isNaN(argv[2])) {
  const loopLimit = Number(argv[2]);
  for (let i = 0; i < loopLimit; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
