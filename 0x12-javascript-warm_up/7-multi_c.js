#!/usr/bin/node

const { argv } = require('node:process');

if (!isNaN(argv[2])) {
  const loop_limit = Number(argv[2]);
  if (loop_limit < 0) {
    return;
  } else {
    for (let i = 0; i < loop_limit; i++) {
      console.log('C is fun');
    }
  }
} else {
    console.log('Missing number of occurrences');
}