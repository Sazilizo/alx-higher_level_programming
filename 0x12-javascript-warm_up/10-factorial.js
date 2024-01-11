#!/usr/bin/node

const { argv } = require('node:process');
const a = parseInt(argv[2]);

function factorial (a) {
  if (a === 0 || (isNaN(argv[2])) || (a < 0)) {
    return 1;
  } else {
    return (a * factorial(a - 1));
  }
}

const fact = factorial(a);
console.log(fact);
