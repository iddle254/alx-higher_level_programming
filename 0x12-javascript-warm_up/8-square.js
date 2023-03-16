#!/usr/bin/node

const x = parseInt(process.argv[2], 10);
let i = x;
if (!isNaN(x) && x > 0) {
  for (i; i !== 0; i--) {
    console.log('X'.repeat(x));
  }
} else if (isNaN(x)) {
  console.log('Missing size');
}
