#!/usr/bin/node

function factorial(n) {
  console.log(n === 0 || isNaN(n) ? 1 : n * factorial(n - 1));
}

factorial(parseInt(process.argv[2]));
