#!/usr/bin/node
const x = parseInt(process.argv[2]);
function factorial (x) {
  if (isNaN(x)) {
    return (1);
  } else {
    return (x * (x - 1));
  }
}

console.log(factorial(x));
