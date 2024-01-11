#!/usr/bin/node

const { argv } = require('node:process');

const loopLimit = parseInt(argv[2]);

if (isNaN(loopLimit)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < loopLimit; i++) {
    console.log('x'.repeat(loopLimit));
  }
}
