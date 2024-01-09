#!/usr/bin/node

const { argv } = require('node:process');

for (let i = 2; i < 3; i++) {
	console.log(`${argv[2]} is ${argv[3]}`);
}
