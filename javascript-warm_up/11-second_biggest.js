#!/usr/bin/node

const args = process.argv.slice(2).map(arg => parseInt(arg));

if (args.length < 2) {
  console.log(0);
} else {
  let max = args[0] > args[1] ? args[0] : args[1];
  let secondMax = args[0] < args[1] ? args[0] : args[1];

  for (let i = 2; i < args.length; i++) {
    if (args[i] > max) {
      secondMax = max;
      max = args[i];
    } else if (args[i] > secondMax) {
      secondMax = args[i];
    }
  }

  console.log(secondMax);
}
