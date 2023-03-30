#!/usr/bin/node
function factorial (b) {
  if ((Number.isNaN(b)) || (b === 1)) {
    return 1;
  }
  return factorial(b - 1) * b;
}

console.log(factorial(parseInt(process.argv[2])));
